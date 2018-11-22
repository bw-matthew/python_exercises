""" Write a python function that takes no arguments,
    but will read the files in the current working directory and return a list of them.
    Test it while in a couple of directories. """
from pathlib import Path


def main():
    """ Prints each file in the current directory """
    for file in Path('.').iterdir():
        print(file)


if __name__ == '__main__':
    main()
