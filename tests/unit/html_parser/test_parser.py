import pytest
from pathlib import Path

from word.builder import AbstractWordBuilder
from html_parser.parser import HtmlParser, HtmlCorruptedError


@pytest.fixture
def word_builder_stub_class():
    class BuilderStub(AbstractWordBuilder):
        def __init__(self) -> None:
            self.buffer = []

        def append_char(self, character: str) -> bool:
            if character in [' ', '\n', '&']:
                return False
            self.buffer.append(character)
            return True
        
        def build(self) -> str:
            return ''.join(self.buffer)
            
        @property        
        def empty(self) -> bool:
            return not self.buffer
    
    return BuilderStub


def get_html_data(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8') as test_file:
        return test_file.read()
    

def test_parser_ignored_tags(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'ignore_tags.html'))
    test_ignored_tags = {"script", "style", "meta"}
    test_entity_name_separators = []
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()

    expected_result = ('HTML', 'Elements', 'Reference', 'My', 'First', 'Heading', 'Article', 'here', 'could', 'be',
                       'unfolded')
    assert result == expected_result


def test_parser_entity_name_separators(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'entity_name_separators.html'))
    test_ignored_tags = set()
    test_entity_name_separators = ['&nbsp;', '&lt;']
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()

    expected_result = ('HTML', 'Elements', 'Reference', 'My', 'First', 'Heading', 'testing', 'Article', 'here', 'could',
                       'be', 'unfolded', 'Data', 'should', 'be', 'read', 'correctly', 'text', 'here', 'other', 'body',
                       'content')
    assert result == expected_result


def test_parser_word_gen(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'read_word_by_word.html'))
    test_ignored_tags = set()
    test_entity_name_separators = []
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    uut_gen = uut.get_word_gen()

    result_1 = next(uut_gen)
    result_2 = next(uut_gen)
    result_3 = next(uut_gen)
    with pytest.raises(Exception) as ex_info:
        next(uut_gen)

    assert result_1 == 'HTML'
    assert result_2 == 'Elements'
    assert result_3 == 'Reference'
    assert isinstance(ex_info.value, StopIteration)


def test_parser_no_words(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'no_words.html'))
    test_ignored_tags = set()
    test_entity_name_separators = []
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()    

    assert result == tuple()


def test_parser_no_end_tag(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'no_tag_ending.html'))
    test_ignored_tags = set()
    test_entity_name_separators = []
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    with pytest.raises(Exception) as ex_info:
        result = uut.get_all_words()    

    assert isinstance(ex_info.value, HtmlCorruptedError)

def test_parser_invalid_entity_name_as_separator(word_builder_stub_class):
    test_data = get_html_data(Path('tests', 'unit', 'html_parser', 'test_html', 'invalid_entity_name_separator.html'))
    test_ignored_tags = set()
    test_entity_name_separators = ['&nbsp;']
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=word_builder_stub_class,
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()    

    assert result == ('One', 'radic;', 'other')