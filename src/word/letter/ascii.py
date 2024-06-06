"""Checks if character is valid part of the ascii-like word
"""
APOSTROPHE_NUM = 39 # Not ideal since the single close quote character can be used as well (&#8217;)
UPPER_A_NUM = 65
UPPER_Z_NUM = 90
LOWER_A_NUM = 97
LOWER_Z_NUM = 122


def is_upper_letter(ascii_number: int) -> bool:
    """Checks if ascii char number matches upper case ascii letter
    :param ascii_number:
    :return: True if uppercase, False otherwise
    """
    if UPPER_Z_NUM >= ascii_number >= UPPER_A_NUM:
        return True
    return False


def is_lower_letter(ascii_number: int) -> bool:
    """Checks if ascii char number matches lower case ascii letter
    :param ascii_number: 
    :return: True if lowercase, False otherwise
    """
    if LOWER_Z_NUM >= ascii_number >= LOWER_A_NUM:
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
    return any((is_lower_letter(ascii_number), is_upper_letter(ascii_number), ascii_number == APOSTROPHE_NUM))
