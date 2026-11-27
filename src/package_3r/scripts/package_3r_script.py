"""CLI script for the package_3r package. This will be called on the command line"""

import click

from package_3r.package_3r import calculate_mean, hello_world


@click.command()
@click.option(
    "--message",
    default=None,
    help="Type a message to say",
)
@click.option(
    "--mean",
    default=None,
    help="Calculate the mean of comma-separated numbers.",
)
@click.version_option()
def package_3r_cli(message, mean):
    """Example script. This function is referenced in setup.cfg."""

    if mean is not None:
        try:
            values = [float(x.strip()) for x in mean.split(",")]
        except ValueError as exc:
            raise click.BadParameter(
                "Please enter comma-separated numbers.",
                param_hint="--mean",
            ) from exc

        result = calculate_mean(values)
        click.echo(f"Mean: {result}")
        return

    if message is not None:
        click.echo(hello_world(message))
        return

    click.echo(click.get_current_context().get_help())
