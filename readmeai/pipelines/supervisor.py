import click
from readmeai.components.init import init_project

@click.group()
def cli():
    pass

@cli.command()
def init():
    init_project()

@cli.command()
def run():
    from readmeai.components.run import run_docs
    run_docs()