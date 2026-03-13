import click
import os
from exo.core.converter import URLConverter
from exo.core.creator import SkillCreator
from exo.core.evolver import SkillEvolver
from exo.utils.helpers import ensure_directory


@click.group()
def cli():
    """EXO - Explore, Extend, Evolve AI Agent Cognition."""
    pass


@cli.command()
@click.option('--url', required=True, help='URL to convert')
@click.option('--name', help='skill name')
@click.option('--output', help='output directory')
def convert(url, name, output):
    """Convert URL to skill"""
    converter = URLConverter()
    skill_dir = converter.convert(url, output)
    click.echo(f"Conversion complete! Skill saved to: {skill_dir}")
    
    # Automatically create skill
    creator = SkillCreator()
    creator.create(skill_dir)
    click.echo(f"Skill creation complete!")


@cli.command()
@click.option('--skill', required=True, help='skill directory')
def evolve(skill):
    """Evolve skill content"""
    evolver = SkillEvolver()
    skill_dir = evolver.evolve(skill)
    click.echo(f"Evolution complete! Skill updated: {skill_dir}")


@cli.command()
@click.option('--urls', required=True, help='File containing URL list')
@click.option('--output', default='./skills', help='output directory')
def batch(urls, output):
    """Batch process URL list"""
    ensure_directory(output)
    
    with open(urls, 'r') as f:
        url_list = [line.strip() for line in f if line.strip()]
    
    converter = URLConverter()
    creator = SkillCreator()
    
    for url in url_list:
        try:
            click.echo(f"Processing URL: {url}")
            skill_dir = converter.convert(url, os.path.join(output, f'skill_{len(os.listdir(output))}'))
            creator.create(skill_dir)
            click.echo(f"Processing complete: {skill_dir}")
        except Exception as e:
            click.echo(f"Processing failed: {str(e)}")


@cli.command()
def version():
    """Show version information"""
    click.echo("EXO v0.1.0")


if __name__ == '__main__':
    cli()
