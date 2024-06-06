"""Dumps result to file
"""
import json


FILENAME = 'result.txt'


def save_to_file(data: dict, filename = FILENAME):
    """Saves dict data to file

    :param data:
    :param filename:
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=2))
        