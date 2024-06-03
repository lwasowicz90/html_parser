"""Implementation of building the word character by character.
"""
import logging
from abc import ABC, abstractmethod
from typing import Callable


class AbstractWordBuilder(ABC):
    """Abstract class for word builder
    """
    @abstractmethod
    def append_char(self, character: str) -> bool:
        """append_char abstract method
        :param character:
        """

    @abstractmethod
    def build(self) -> str:
        """build abstract method
        :return:
        """

    @property
    @abstractmethod
    def empty(self) -> bool:
        """empty abstract method        
        :return:
        """


class IWordBuilder(AbstractWordBuilder):
    """Interface for word builder
    """

    def __init__(self, letter_validator: Callable[[str], bool]) -> None:
        """Initializes WordBuilder instance
        :param letter_validator: Predicate that validates if character to append is valid
        """
        self._letter_validator = letter_validator
        self._buffer = []
        self._is_constructed = False
        self._logger = logging.getLogger(f'{IWordBuilder.__name__}[{hex(id(self))}]')

    def append_char(self, character: str) -> bool:
        """Appends character to the buffer
        :param character: _description_
        :raises OverflowError: if build method was called before appending
        :return: True on success, False if character failed validation
        """
        if self._is_constructed:
            raise OverflowError(
                "There is already word constructed! Cannot add another character!")

        if not self._letter_validator(character):
            self._logger.debug('Character is not valid: %s', character)
            return False
        self._buffer.append(character)
        self._logger.debug('Appended %s ', character)
        return True

    def build(self) -> str:
        """Creates string from buffer
           It is caller responsibility to check if buffer is not empty in order to avoid
           empty word.
        :raises RuntimeError: if already constructed
        :return: constructed word
        """
        if self._is_constructed:
            raise RuntimeError('The word has been already built.')
        result =  ''.join(self._buffer)
        self._is_constructed = True
        self._logger.debug('Built %s', result)
        return result

    @property
    def empty(self) -> bool:
        """Check if buffer is empty
        :return: True if buffer empty, False otherwise
        """
        return not self._buffer
