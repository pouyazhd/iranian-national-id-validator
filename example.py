"""laus deo
iranian national ID checker and generator
"""

import argparse
from random import randint

from inid_validator import IranianNatioanlID

parser = argparse.ArgumentParser(
    description="check valid Iranian National ID or generate a fake one."
)
parser.add_argument(
    "-c",
    "--check",
    required=False,
    type=str,
    dest="check",
    help="check the id is correct or not. returns True or False. Example: -c 1234567890, ",
)
parser.add_argument(
    "-g",
    "--generate",
    type=bool,
    required=False,
    default=False,
    dest="generate",
    help="generate a fake iranian national ID. Example: -g True",
)

args = parser.parse_args()

def main():

    national_id = IranianNatioanlID()
    try:
        if args.generate:
            print("generated id:")
            print(national_id.new_id)
        else:
            print(f"check validation id {args.check}:")
            print(national_id.validation_check(args.check))
    except Exception as err:
        print(f"Exception happened: {err}")


if __name__ == "__main__":
    main()
