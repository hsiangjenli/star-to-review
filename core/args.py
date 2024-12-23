"""Command-line arguments parser."""

from argparse import ArgumentParser


def parse_args():
    """Parse command-line arguments."""
    args = ArgumentParser()

    args.add_argument("--github-username", required=True, help="GitHub username")
    args.add_argument(
        "--devel", required=False, type=bool, default=False, help="Development mode"
    )

    args = args.parse_args()

    return args
