"""Calculates number of words
"""
from collections import Counter


def get_occurences(words: tuple[str]):
    """Calculates number of occurences of given word in datataset
    :param words: dataset
    :return: dictionary, word: num occurences
    """
    return Counter(words)


def get_top_n_occurences(words: tuple[str], top_n: int, descending: bool=True):
    """Returns top n words in dataset in specified order
    :param words: words dataset
    :param n: top n results to get
    :param descending:
    """
    occurences = get_occurences(words)
    sorted_keys_top_n = sorted(occurences, key=occurences.get, reverse=descending)[:top_n]
    
    return {key : occurences[key] for key in sorted_keys_top_n}
