import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent


def validate_parameters(service, env):
    if service not in ["api", "client"]:
        print("Invalid service name")
        sys.exit(1)
    if env not in ["development", "production"]:
        print("Invalid env name")
        sys.exit(1)
