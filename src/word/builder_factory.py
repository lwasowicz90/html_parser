"""Provides function to create word builder object to be injected to html parser
"""
from enum import Enum

from word.builder import IWordBuilder
from word.letter.ascii import is_valid as is_valid_ascii


class WordBuilderPolicy(Enum):
    """Lists all word policies as enum class    
    """
    ENGLISH_WORD_POLICY = 1


def create(policy: WordBuilderPolicy) -> IWordBuilder:
    """factory function for word builder
    :param policy: policy
    :return: constructer instance of IWordBuilder
    """
    match policy:
        case WordBuilderPolicy.ENGLISH_WORD_POLICY:
            return IWordBuilder(is_valid_ascii)
