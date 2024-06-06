"""Provides function to create word builder object to be injected to html parser
"""
from enum import Enum

from word.builder import IWordBuilder
from word.letter.ascii import is_valid as is_valid_ascii
from word.letter.unicode import is_valid as is_valid_unicode


class WordBuilderPolicy(Enum):
    """Lists all word policies as enum class    
    """
    ENGLISH_WORD_POLICY = 1
    LATIN_LANGUAGE_POLICY = 2


def create(policy: WordBuilderPolicy) -> IWordBuilder:
    """factory function for word builder
    :param policy: policy
    :raises: ValueError if incorrect policy
    :return: constructer instance of IWordBuilder
    """
    match policy:
        case WordBuilderPolicy.ENGLISH_WORD_POLICY:
            return IWordBuilder(is_valid_ascii)
        case WordBuilderPolicy.LATIN_LANGUAGE_POLICY:
            return IWordBuilder(is_valid_unicode)
        case _:
            raise ValueError('Incorrect builder choice')
