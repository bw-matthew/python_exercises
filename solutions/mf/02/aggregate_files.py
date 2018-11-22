""" Read in the given three files, a csv file, a json file, and a pickle file.
    Calculate a summary.
    Write the files as a single json file. """
import argparse
import pickle

import pandas


def main():
    """ Reads three files and aggregates them """
    parser = argparse.ArgumentParser()
    parser.add_argument('--in-csv')
    parser.add_argument('--in-json')
    parser.add_argument('--in-pickle')
    parser.add_argument('--in-excel')
    parser.add_argument('--out', required=True)
    arguments = parser.parse_args()

    frames = []
    if arguments.in_csv is not None:
        frames.append(pandas.read_csv(arguments.in_csv))

    if arguments.in_json is not None:
        frames.append(pandas.read_json(arguments.in_json))

    if arguments.in_pickle is not None:
        with open(arguments.in_pickle, 'rb') as handle:
            frames.append(pickle.load(handle))

    if arguments.in_excel is not None:
        frames.append(pandas.read_excel(arguments.in_excel))

    assert frames, 'must provide at least one input file'

    merged_data = frames[0]
    for current in frames[1:]:
        merged_data = merged_data.merge(current)
    merged_data.to_json(arguments.out)


def merge_all(*entries):
    """ Merge all arguments together """
    left = entries[0]
    for right in entries[1:]:
        left = merge(left, right)
    return left


def merge(left, right):
    """ Simple shallow merge of data structures.
        Lists are concatenated.
        Dictionaries are merged by key.
        The left is preferred to the right. """
    if isinstance(left, list):
        assert isinstance(right, list)
        return left + right
    if isinstance(left, dict):
        assert isinstance(right, dict)
        combined = right.copy()
        combined.update(left)
        return combined
    return left


if __name__ == '__main__':
    main()
