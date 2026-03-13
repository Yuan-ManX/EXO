# Examples

Here are practical examples of using EXO for various tasks.

## Example 1: URL to Markdown Conversion

### Basic Conversion

```python
from exo import EXO

exo = EXO()

# Convert a web page
content = exo.convert_url("https://example.com")

# Save to file
with open("output.md", "w") as f:
    f.write(content)
```

### With Crawler

```python
from exo import convert

# Convert and download all resources
content = convert("https://example.com", use_crawler=True)
print("Page converted and resources downloaded!")
```

### CLI Version

```bash
exo convert https://example.com -o page.md --crawler
```

## Example 2: Creating a Skill

### Data Processing Skill

```python
from exo import create

skill = create(
    """
    A skill that reads JSON data from a file,
    extracts specific fields, and generates a summary report.
    
    Requirements:
    - Handle large JSON files efficiently
    - Support multiple output formats (text, CSV)
    - Include error handling for invalid JSON
    """
)

print(skill)
```

### Web Scraping Skill

```python
from exo import EXO

exo = EXO()

skill = exo.create_skill(
    "A web scraper that extracts product information from e-commerce sites",
    name="product-scraper"
)

# Save to file
with open("skills/product_scraper.py", "w") as f:
    f.write(skill)
```

## Example 3: Evolving a Skill

### Simple Evolution

```python
from exo import evolve

# Improve an existing skill
evolved_skill = evolve(
    "skills/my-skill.py",
    "Add logging to track what the skill is doing"
)

# Save the improved version
with open("skills/my-skill-improved.py", "w") as f:
    f.write(evolved_skill)
```

### Multiple Iterations with Engine

```python
from exo import EXO

exo = EXO()

# Use the advanced evolution engine for better results
final_skill = exo.evolve_skill(
    "skills/data-processor.py",
    "Optimize for speed and memory efficiency with large datasets",
    use_engine=True,
    iterations=5
)
```

## Example 4: Using the Evolution Engine Directly

```python
from exo.core.evolution_engine import EvolutionEngine

# Create the engine
engine = EvolutionEngine(
    model="openai/gpt-5.4",
    max_iterations=5
)

# Define your initial candidate
initial_skill = """
def process_data(data):
    return [x * 2 for x in data]
"""

# Define evaluation tasks
tasks = [
    {"input": [1, 2, 3], "expected": [2, 4, 6]},
    {"input": [0, -1, 5], "expected": [0, -2, 10]}
]

# Define evaluator
def evaluator(candidate, task):
    # Execute the candidate code and evaluate
    # This is a simplified example
    try:
        exec(candidate, globals())
        result = process_data(task["input"])
        score = 1.0 if result == task["expected"] else 0.0
        return score, f"Result: {result}"
    except Exception as e:
        return 0.0, f"Error: {str(e)}"

# Run evolution
result = engine.evolve(
    initial_candidate=initial_skill,
    tasks=tasks,
    evaluator=evaluator
)

print(f"Best skill:\n{result.best_candidate}")
print(f"Best score: {result.best_score}")
```

## Example 5: Web Crawler Usage

```python
from exo.core.crawler import WebCrawler

# Initialize crawler
crawler = WebCrawler(output_dir="./my-downloads")

# Crawl a website
resource = crawler.crawl("https://example.com")

# Print information
print(f"Title: {resource.title}")
print(f"URL: {resource.url}")
print(f"Number of images: {len(resource.images)}")
print(f"Number of CSS files: {len(resource.css_files)}")
print(f"Number of JS files: {len(resource.js_files)}")

# Access downloaded files
print(f"\nDownloaded files in: {resource.download_dir}")
for img in resource.images:
    print(f"  - {img}")
```

## Example 6: Complete Workflow

```python
from exo import EXO

def main():
    # Initialize EXO
    exo = EXO(model="openai/gpt-5.4")
    
    # Step 1: Convert and download documentation
    print("Converting documentation...")
    docs = exo.convert_url(
        "https://example.com/docs",
        use_crawler=True
    )
    
    # Step 2: Create a skill based on the docs
    print("Creating skill...")
    skill = exo.create_skill(
        f"Create a skill that uses the API documented here:\n{docs}",
        name="api-client"
    )
    
    with open("skills/api_client.py", "w") as f:
        f.write(skill)
    
    # Step 3: Evolve and improve the skill
    print("Evolving skill...")
    final_skill = exo.evolve_skill(
        "skills/api_client.py",
        "Add rate limiting, retries, and comprehensive error handling",
        iterations=3
    )
    
    with open("skills/api_client_final.py", "w") as f:
        f.write(final_skill)
    
    print("Workflow complete!")

if __name__ == "__main__":
    main()
```

## Example 7: Batch Processing

```python
from exo import convert

# List of URLs to process
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

# Process each URL
for i, url in enumerate(urls):
    print(f"Processing {i+1}/{len(urls)}: {url}")
    content = convert(url, use_crawler=True)
    with open(f"output/page_{i+1}.md", "w") as f:
        f.write(content)

print("All URLs processed!")
```

## Example 8: Integration with Other Tools

```python
from exo import EXO
import git
import os

exo = EXO()

def process_repo_docs(repo_url, local_path):
    # Clone the repo
    if not os.path.exists(local_path):
        git.Repo.clone_from(repo_url, local_path)
    
    # Find and convert README
    readme_path = os.path.join(local_path, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r") as f:
            content = f.read()
        
        # Create a skill based on the README
        skill = exo.create_skill(
            f"Create a skill that demonstrates the usage of this project:\n{content}"
        )
        
        skill_path = os.path.join(local_path, "exo_skill.py")
        with open(skill_path, "w") as f:
            f.write(skill)
        
        print(f"Created skill at: {skill_path}")

# Usage
process_repo_docs(
    "https://github.com/example/project.git",
    "./temp-project"
)
```
