# API Reference

EXO provides both a high-level Python API and a CLI interface for maximum flexibility.

## Python API

### The `EXO` Class

The main entry point for all EXO functionality.

```python
from exo import EXO

# Initialize with default settings
exo = EXO()

# Or with custom configuration
exo = EXO(
    model_provider="openrouter",
    model="openai/gpt-5.4",
    api_key="your-api-key"
)
```

#### Methods

##### `convert_url(url, output_path=None, use_crawler=False)`

Convert a web URL to Markdown format.

**Parameters:**
- `url` (str): The URL to convert
- `output_path` (str, optional): Path to save the output file
- `use_crawler` (bool, optional): If True, also downloads all web resources

**Returns:**
- `str`: The converted Markdown content

**Example:**
```python
content = exo.convert_url("https://example.com", use_crawler=True)
```

##### `create_skill(prompt, name=None, output_path=None)`

Create a new skill using LLM.

**Parameters:**
- `prompt` (str): Description of what the skill should do
- `name` (str, optional): Name for the skill
- `output_path` (str, optional): Path to save the skill file

**Returns:**
- `str`: The generated skill content

**Example:**
```python
skill = exo.create_skill(
    "A skill that analyzes CSV files and generates summary reports",
    name="csv-analyzer"
)
```

##### `evolve_skill(skill_path, prompt, use_engine=True, iterations=3)`

Evolve and improve an existing skill.

**Parameters:**
- `skill_path` (str): Path to the skill file
- `prompt` (str): Evolution instructions or feedback
- `use_engine` (bool, optional): Use the advanced evolution engine (default: True)
- `iterations` (int, optional): Number of evolution iterations (default: 3)

**Returns:**
- `str`: The evolved skill content

**Example:**
```python
evolved = exo.evolve_skill(
    "skills/my-skill.py",
    "Make it handle large files more efficiently",
    use_engine=True,
    iterations=5
)
```

##### `process(input_data, operation, **kwargs)`

Generic method for any EXO operation.

**Parameters:**
- `input_data`: The input data to process
- `operation` (str): The operation to perform ('convert', 'create', 'evolve')
- `**kwargs`: Additional operation-specific parameters

**Returns:**
- The result of the operation

### Convenience Functions

For quick access without instantiating the class:

```python
from exo import convert, create, evolve, process

# Convert a URL
content = convert("https://example.com")

# Create a skill
skill = create("A skill that translates text")

# Evolve a skill
evolved = evolve("skills/translator.py", "Add French support")
```

### Evolution Engine

#### `EvolutionEngine`

The advanced evolution engine inspired by GEPA.

```python
from exo.core.evolution_engine import EvolutionEngine

engine = EvolutionEngine(
    model="openai/gpt-5.4",
    max_iterations=5
)

result = engine.evolve(
    initial_candidate=initial_skill,
    tasks=evaluation_tasks,
    evaluator=your_evaluator_function
)
```

### Web Crawler

#### `WebCrawler`

Comprehensive web crawling functionality.

```python
from exo.core.crawler import WebCrawler

crawler = WebCrawler(output_dir="./downloads")
resource = crawler.crawl("https://example.com")

print(f"Title: {resource.title}")
print(f"HTML: {resource.html_content[:100]}...")
print(f"Images downloaded: {len(resource.images)}")
```

### Core Classes

#### `URLConverter`

Handles URL to Markdown conversion.

```python
from exo.core.converter import URLConverter

converter = URLConverter()
markdown = converter.convert("https://example.com")
```

#### `SkillCreator`

Generates new skills from descriptions.

```python
from exo.core.creator import SkillCreator

creator = SkillCreator()
skill = creator.create(
    "A skill that fetches weather data",
    requirements=["requests"]
)
```

#### `SkillEvolver`

Evolves existing skills with feedback.

```python
from exo.core.evolver import SkillEvolver

evolver = SkillEvolver()
new_skill = evolver.evolve(
    "skills/old-skill.py",
    "Improve error handling"
)
```

## Configuration

### Environment Variables

- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `EXO_MODEL_PROVIDER`: Default model provider ('openrouter')
- `EXO_MODEL`: Default model to use

### Model Configuration

EXO supports any model available through OpenRouter. Popular choices:
- `openai/gpt-5.4` (default, good balance of cost and quality)
- `openai/gpt-5.4` (best quality)
- `anthropic/claude-4-6-sonnet`
- `google/gemini-3-pro`

## Error Handling

```python
from exo import EXO

exo = EXO()

try:
    content = exo.convert_url("https://example.com")
except Exception as e:
    print(f"Error: {e}")
    # Handle error appropriately
```
