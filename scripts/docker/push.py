import subprocess


from common import validate_parameters

import click


@click.command()
@click.option(
    "--service",
    type=click.STRING,
    required=True,
    help="Pass <service> list to build docker images (ex. api, client...)",
)
@click.option(
    "--env",
    type=click.STRING,
    default="development",
    help="Pass <env> to build docker images (ex. development, production ...)",
)
def push(service, env):
    validate_parameters(service, env)
    """Push the Docker image."""
    # Push the Docker image.
    image_tag = f"parkyes90/edep-{service}-{env}:latest"
    print("Pushing the Docker image...")
    subprocess.run(
        [
            "docker",
            "push",
            image_tag,
        ],
        check=True,
    )
    print("Success!")


if __name__ == "__main__":
    push()
