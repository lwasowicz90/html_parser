"""Dumps result to file
"""
FILENAME = 'result.txt'


def save_to_file(data: dict, filename = FILENAME):
    """Saves dict data to file

    :param data:
    :param filename:
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(data))
