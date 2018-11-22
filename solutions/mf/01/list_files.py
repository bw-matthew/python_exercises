""" Edit that code to take in two arguments,
    one for the directory and another for the file extension pattern.
    Test it. """
import argparse
from pathlib import Path


def main():
    """ Prints each file in the desired directory with the required extension """
    parser = argparse.ArgumentParser()
    parser.add_argument('DIRECTORY')
    parser.add_argument('EXTENSION')
    arguments = parser.parse_args()

    for file in Path(arguments.DIRECTORY).iterdir():
        if file.name.endswith(f'.{arguments.EXTENSION}'):
            print(file)


if __name__ == '__main__':
    main()
