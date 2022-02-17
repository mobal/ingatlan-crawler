import argparse
import encodings
import logging
import os
import yaml

loggin = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument(
    "-c",
    "--config",
    default="default.yml",
    metavar="file",
    type=str,
    help="Path to the configuration file",
)

args = parser.parse_args()


def _load_configuration(f: str):
    with open(os.path.abspath(f), encoding=encodings.utf_8.getregentry().name) as s:
        try:
            return yaml.safe_load(s)
        except yaml.YAMLError as error:
            raise error


def main():
    result = _load_configuration(args.config)
    print(result)


if __name__ == "__main__":
    main()
