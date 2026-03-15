from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="octopai",
    version="0.1.0",
    description="Octopai - Explore, Extend, Evolve AI Agent Cognition.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yuan Man",
    url="https://github.com/Yuan-ManX/octopai",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "click>=8.1.7",
        "python-dotenv>=1.0.0",
        "markdown>=3.4.3",
        "beautifulsoup4>=4.12.2",
        "PyPDF2>=3.0.0",
        "python-docx>=1.1.0",
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
        "Pillow>=10.0.0",
        "opencv-python>=4.8.0",
        "PyYAML>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "octopai=octopai.cli.main:cli"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.8',
    keywords="ai, agent, skill, evolution, llm, openrouter",
)
