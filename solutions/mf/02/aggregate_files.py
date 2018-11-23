""" Read in the given three files, a csv file, a json file, and a pickle file.
    Calculate a summary.
    Write the files as a single json file. """
import argparse
import pickle

import pandas


def main():
    """ Reads a number of files and aggregates them """
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='+')
    parser.add_argument('output')
    arguments = parser.parse_args()

    readers = {
        'csv': read_csv,
        'json': read_json,
        'xlsx': read_excel,
        'pickle': read_pickle,
    }

    frames = [readers[get_extension(file)](file) for file in arguments.input]

    merged_data = frames[0]
    for current in frames[1:]:
        merged_data = merged_data.merge(current)

    merged_data.to_json(arguments.output)


def get_extension(file):
    """ Get the extension of the file.
        Will lower case the result for ease of comparison. """
    try:
        return file[file.rindex('.') + 1:].lower()
    except ValueError:
        raise ValueError(
            f'Filename {file} has no extension - cannot infer reader')


def read_csv(file):
    """ Read a CSV file into a data frame """
    return pandas.read_csv(file)


def read_json(file):
    """ Read a json file into a data frame """
    return pandas.read_json(file)


def read_excel(file):
    """ Read an excel file into a data frame """
    return pandas.read_excel(file)


def read_pickle(file):
    """ Read a pickle file into a python object """
    with open(file, 'rb') as handle:
        return pickle.load(handle)


if __name__ == '__main__':
    main()
