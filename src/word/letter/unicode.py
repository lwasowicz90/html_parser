"""Module to validate utf-8 letters
Logic based on https://en.wikipedia.org/wiki/List_of_Unicode_characters
"""
from word.letter.ascii import (is_lower_letter as is_ascii_lower_letter,
                               is_upper_letter as is_ascii_upper_letter,
                               APOSTROPHE_NUM)


APOSTROPHE_AS_RIGHT_SINGLE_QUOT_MARK_NUM = int('0x2019', 0)

UPPER_LATIN1_SUPLEMENT_START_1 = int('0x00C0', 0)
UPPER_LATIN1_SUPLEMENT_END_1 = int('0x00D6', 0)
UPPER_LATIN1_SUPLEMENT_START_2 = int('0x00D8', 0)
UPPER_LATIN1_SUPLEMENT_END_2 = int('0x00DE', 0)

LOWER_LATIN1_SUPLEMENT_START_1 = int('0x00DF', 0)
LOWER_LATIN1_SUPLEMENT_END_1 = int('0x00F6', 0)
LOWER_LATIN1_SUPLEMENT_START_2 = int('0x00F8', 0)
LOWER_LATIN1_SUPLEMENT_END_2 = int('0x00FF', 0)

EU_LATIN_EXTENDED_A_START = int('0x0100', 0)
EU_LATIN_EXTENDED_A_END = int('0x017F', 0)

LATIN_EXTENDED_B_START = int('0x0180', 0)
LATIN_EXTENDED_B_END = int('0x024F', 0)


def is_upper_latin1_sup_letter(ascii_number: int) -> bool:
    """Checks if char number matches upper case Latin1 suplement 1 letter
    :param ascii_number:
    :return:
    """
    if any([UPPER_LATIN1_SUPLEMENT_END_1 >= ascii_number >= UPPER_LATIN1_SUPLEMENT_START_1,
            UPPER_LATIN1_SUPLEMENT_END_2 >= ascii_number >= UPPER_LATIN1_SUPLEMENT_START_2]):
        return True
    return False


def is_lower_latin1_sup_letter(ascii_number: int) -> bool:
    """Checks if char number matches lower case Latin1 suplement 1 letter
    :param ascii_number:
    :return: True if uppercase, False otherwise
    """
    if any([LOWER_LATIN1_SUPLEMENT_END_1 >= ascii_number >= LOWER_LATIN1_SUPLEMENT_START_1,
            LOWER_LATIN1_SUPLEMENT_END_2 >= ascii_number >= LOWER_LATIN1_SUPLEMENT_START_2]):
        return True
    return False


def is_eu_latin_extended_a_letter(ascii_number: int) -> bool:
    """Checks if ascii char number matches eu latin extended a letter
    :param ascii_number: 
    :return:
    """
    if EU_LATIN_EXTENDED_A_END >= ascii_number >= EU_LATIN_EXTENDED_A_START:
        return True
    return False


def is_latin_extended_b_letter(ascii_number: int) -> bool:
    """Checks if ascii char number matches latin extended b letter
    :param ascii_number: 
    :return:
    """
    if LATIN_EXTENDED_B_END >= ascii_number >= LATIN_EXTENDED_B_START:
        return True
    return False


def is_valid(character: str) -> bool:
    """Checks if character can be part of the word
    :param character: char to check 
    :return: True if valid, False otherwise
    """

    if len(character) != 1:
        raise ValueError("It supports only single character string!")

    ascii_number = ord(character)
    return any((is_ascii_lower_letter(ascii_number),
                is_ascii_upper_letter(ascii_number),
                ascii_number == APOSTROPHE_NUM,
                ascii_number == APOSTROPHE_AS_RIGHT_SINGLE_QUOT_MARK_NUM,
                is_lower_latin1_sup_letter(ascii_number),
                is_upper_latin1_sup_letter(ascii_number),
                is_eu_latin_extended_a_letter(ascii_number),
                is_latin_extended_b_letter(ascii_number)))
