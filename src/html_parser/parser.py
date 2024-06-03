"""Implementation of html parser to extract human readable text from html page
"""
import logging

from typing import Callable, Generator
from word.builder import AbstractWordBuilder


class HtmlCorruptedError(Exception):
    pass


class HtmlParser:
    """Parses html page, lazy calc
    """
    ENDING_TAG_SLASH_IDX = 1

    def __init__(self,
                 html_data: str,
                 create_word_builder: Callable[[None], AbstractWordBuilder],
                 tags_ignored: set[str],
                 entity_name_separators: list[str]
                 ):
        """
        :param html_data: html page as string data
        :param create_word_builder: callable to create word builder
        :param tags_ignored: set of tags to be ignored from reading the content
        :param entity_name_separators: list of html entity names that acts as word separator
        """
        self._data = html_data
        self._size = len(self._data)
        self._current_idx = 0
        self._create_word_builder = create_word_builder
        self._tags_ignored = tags_ignored
        self._entity_name_separators = entity_name_separators
        self._logger = logging.getLogger(HtmlParser.__name__)

    def get_word_gen(self)-> Generator[str, None, None]:
        """Generator for reading words for lazy reading.           
        :yield: single word
        """
        while word:= self._get_next_word():
            yield word

    def get_all_words(self) -> tuple[str]:
        """Reads all words from html data          
        :return tuple with words
        """
        return tuple(word for word in self.get_word_gen())

    def _get_next_word(self) -> str | None:
        """Reads next word from html data.
           It constructs new word when builder is not empty and:
            - encounters new opening tag
            - if appending to buffer failed (it treats it as 1 character separator e.g "test " should extract "test", 
              the same for "test*", "test@"then "data" where space is separator or test@data or test*data,
            If it finds new tag but builder is empty, it move index to end of the tag.
            If reads data not being in the tag and finds & character it look for matching entity names (suggests to
            use most common entity names like &nbsp;', '&lt;', '&gt;', '&amp;), if found, moves index at the end of 
            entity name
        """
        is_in_tag: bool = False
        skip_data: bool = False
        builder: AbstractWordBuilder = self._create_word_builder()
        while self._current_idx < self._size:
            if self._is_tag_start(self._current_idx): # Found <                
                if not builder.empty:
                    self._logger.debug('Found start tag and builder not empty. Builidng...')
                    return builder.build()
                is_in_tag = True
                start_tag_idx = self._current_idx
                end_tag_idx = self._find_tag_end_idx(start_tag_idx)
                self._current_idx = end_tag_idx
                is_in_tag = False
                tag_name = self._get_tag_name(start_tag_idx, end_tag_idx) # Found >
                self._logger.debug('Found tag %s', tag_name)
                if tag_name in self._tags_ignored:
                    skip_data = True
                elif tag_name[0] == '/' and tag_name[HtmlParser.ENDING_TAG_SLASH_IDX:] in self._tags_ignored:
                    skip_data = False

            elif not skip_data and not is_in_tag:
                character = self._data[self._current_idx]
                is_appended = builder.append_char(character)
                if not is_appended:
                    if not builder.empty:
                        return builder.build()
                    if character == '&':
                        entity_separator = self._find_entity_name_separator(self._current_idx)
                        if entity_separator:
                            self._logger.debug('Found entity name separator %s', entity_separator)
                            self._current_idx += len(entity_separator)
                            continue
            self._current_idx += 1
        return None

    def _is_tag_start(self, idx: int) -> bool:
        """Checks if given data keeps opening tag character for given index
        :param idx:
        :return:
        """
        return self._data[idx] == '<'

    def _find_tag_end_idx(self, start_idx: int) -> int:
        """Finds index of ending tag character
        :param start_idx: 
        :return: index of end of tag character
        """
        idx = start_idx
        try:
            while  self._data[idx] != '>':
                idx += 1
        except IndexError as ex:
            message = 'Cannot find ending tag. Rethrowing...'
            self._logger.error(message, exc_info=True)
            raise HtmlCorruptedError(message) from ex
        return idx

    def _get_tag_name(self, start_tag_idx: int, end_tag_idx: int) -> str:
        """Extracts tag name from data betweem given indexes
        :param start_tag_idx: 
        :param end_tag_idx: 
        :raises ValueError: when indexes do not represent < and >
        :return: tag name
        """
        if self._data[start_tag_idx] != '<' or self._data[end_tag_idx] != '>':
            raise ValueError('Given index range do not represent valid tag')
        return self._data[start_tag_idx+1:end_tag_idx].split()[0]

    def _find_entity_name_separator(self, start_idx: int) -> str:
        """Finds entity name from entity name list
        :param start_idx: 
        :return:
        """
        for entity_name in self._entity_name_separators:
            try:
                candidate = self._data[start_idx:start_idx+len(entity_name)]
            except IndexError:
                self._logger.error('Reading the tag candidate exceedes data size', exc_info=True)
                continue
            if candidate == entity_name:
                return candidate
        return None
