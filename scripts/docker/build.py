import sys
import subprocess
from pathlib import Path

import click

from common import ROOT_DIR


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
def build(service, env):
    if service not in ["api", "client"]:
        print("Invalid service name")
        sys.exit(1)
    if env not in ["development", "production"]:
        print("Invalid env name")
        sys.exit(1)
    print(ROOT_DIR)

    """Builds the Docker image."""
    # Build the Docker image.
    image_tag = f"parkyes90/edep-{service}-{env}:latest"
    print("Building the Docker image...")
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            image_tag,
            "--target",
            env,
            f"{Path(ROOT_DIR, 'services', service)}",
        ],
        check=True,
    )

    # Get the Docker image ID.
    print("Getting the Docker image ID...")
    image_id = (
        subprocess.check_output(["docker", "images", "-q", image_tag])
        .decode("utf-8")
        .strip()
    )

    # Print the Docker image ID.
    print("Docker image ID: " + image_id)

    # Write the Docker image ID to the file.
    # Print a success message.
    print("Success!")


if __name__ == "__main__":
    build()
