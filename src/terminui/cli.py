import click
from terminui import dev

@click.group()
def main():
    pass

main.add_command(dev.dev)
