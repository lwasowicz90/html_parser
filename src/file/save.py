"""Dumps result to file
"""
import json


FILENAME = 'result.txt'


def save_to_file(data: dict, filename = FILENAME):
    """Saves data to file in json format

    :param data:
    :param filename:
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
