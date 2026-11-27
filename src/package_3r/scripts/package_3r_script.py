"""CLI script for the package_3r package. This will be called on the command line"""

import click

from package_3r.package_3r import hello_world


@click.command()
@click.option("--message", prompt="message", help="Type a message to say")
@click.version_option()
def package_3r_cli(message):
    """Example script. This function is referenced in setup.cfg"""
    click.echo(hello_world(message))
