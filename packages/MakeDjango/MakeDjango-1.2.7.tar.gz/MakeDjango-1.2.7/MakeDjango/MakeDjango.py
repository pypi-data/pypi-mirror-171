#!/usr/local/bin/python
import argparse
import os

from .core.processor import Main


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="Make Django",
        description="Quick creation of Django project template",
        epilog="Good Luck...",
    )

    # optional arguments:
    parser.add_argument("-v", "--version", action="store_true", help="package version")
    parser.add_argument("--venv", action="store_true", help="Create venv")
    parser.add_argument("--pack", nargs="*", help="Package names")
    # positional arguments:
    parser.add_argument("name", nargs="?", help="project name")
    parser.add_argument("framework", nargs="?", choices=("rest", "graphql", "django"), help="select your framework")
    parser.add_argument("appnames", nargs="*", help="app names create apps")
    # modes:
    modes = parser.add_mutually_exclusive_group(required=False)
    modes.add_argument("-a", "--auto", action="store_true", help="Auto Template")
    modes.add_argument("-c", "--custom", action="store_true", help="Custom Template")
    # other:
    other = parser.add_argument_group(title="other options:")
    other.add_argument("-d", "--dockerize", action="store_true", help="Dockerize Project")
    other.add_argument("-p", "--path", nargs=1, default=os.getcwd(), help="project directory path")

    args = parser.parse_args()

    if vars(args)["version"]:
        print("1.2.7")
    else:
        Main(parser, **vars(args))


if __name__ == "__main__":
    main()
