import os
import requests
from exo.utils.config import Config
from exo.utils.helpers import read_file, write_file
from exo.core.evolution_engine import EvolutionEngine


class SkillEvolver:
    """Skill self-evolution class"""
    
    def __init__(self):
        self.config = Config()
        self.evolution_engine = EvolutionEngine()
    
    def evolve(self, skill_dir, use_engine: bool = True, iterations: int = 3):
        """
        Evolve skill content
        
        Args:
            skill_dir: Path to the skill directory
            use_engine: Whether to use the advanced evolution engine (default: True)
            iterations: Number of evolution iterations (only for engine mode)
            
        Returns:
            Path to the evolved skill directory
        """
        # Validate configuration
        self.config.validate()
        
        # Read SKILL.md file
        skill_file = os.path.join(skill_dir, 'SKILL.md')
        if not os.path.exists(skill_file):
            raise Exception(f"SKILL.md file not found: {skill_file}")
        
        if use_engine:
            # Use the advanced evolution engine
            return self.evolution_engine.evolve(skill_dir, max_iterations=iterations)
        else:
            # Use the original simple method
            skill_content = read_file(skill_file)
            optimized_content = self._optimize_with_gepa(skill_content)
            write_file(skill_file, optimized_content)
            self._generate_evolution_record(skill_dir)
            return skill_dir
    
    def _optimize_with_gepa(self, content):
        """Optimize skill content using GEPA"""
        # Build GEPA optimization request
        headers = {
            'Content-Type': 'application/json'
        }
        
        data = {
            "prompt": content,
            "target": "ai_agent_skill",
            "optimization_level": "aggressive"
        }
        
        try:
            response = requests.post(
                self.config.GEPA_API_URL,
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            return result.get('optimized_prompt', content)
        except Exception as e:
            print(f"GEPA API call failed, using OpenRouter as fallback: {str(e)}")
            return self._optimize_with_openrouter(content)
    
    def _optimize_with_openrouter(self, content):
        """Use OpenRouter as fallback for GEPA"""
        headers = {
            'Authorization': f'Bearer {self.config.OPENROUTER_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": "anthropic/claude-4.6-opus",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an AI Agent skill optimization expert, responsible for optimizing skill content through self-recursive methods to make it more suitable for AI Agent understanding and use."
                },
                {
                    "role": "user",
                    "content": f"Please optimize the following skill content through self-recursive methods to make it more suitable for AI Agent understanding and use:\n\n{content}"
                }
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                self.config.OPENROUTER_API_URL,
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            return result.get('choices', [{}])[0].get('message', {}).get('content', content)
        except Exception as e:
            print(f"OpenRouter API call failed, using original content: {str(e)}")
            return content
    
    def _generate_evolution_record(self, skill_dir):
        """Generate evolution record"""
        import datetime
        record_dir = os.path.join(skill_dir, 'references', 'evolution')
        os.makedirs(record_dir, exist_ok=True)
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        record_file = os.path.join(record_dir, f'evolution_{timestamp}.md')
        
        record_content = f"""
# Evolution Record

## Evolution Time
{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Evolution Description
Skill content has been evolved through self-optimization, enhancing AI Agent understanding and usage experience.
"""
        write_file(record_file, record_content.strip())
