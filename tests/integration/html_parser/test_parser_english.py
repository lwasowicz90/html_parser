from pathlib import Path

from word.builder_factory import create, WordBuilderPolicy
from html_parser.parser import HtmlParser


def get_html_data(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8') as test_file:
        return test_file.read()


def test_parser_with_english_letters():
    test_data = get_html_data(Path('tests', 'integration', 'html_parser', 'test_html', 'english.html'))
    test_ignored_tags = {"script", "style", "meta"}
    test_entity_name_separators = ["&nbsp;", "&lt;", "&gt;", "&amp;"]
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=lambda: create(WordBuilderPolicy.ENGLISH_WORD_POLICY),
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()
    print(result)
    expected_result = ('Some', 'title', 'My', 'First', 'Heading', 'My', 'first', 'paragraph', 'lol', 'lolx', 'lolx', 'text', 'hesre',
                       'myDo', 'llar', 'text', 'text', 'text', 'kul', 'bul', 'pul', 'pp', 'taki', 'test', 'com', 'taki',
                       'test', 'com', 'egrave', 'lnothingfancy', 'data', "one's", "two's", 'five')
    assert result == expected_result


def test_parsing_real_page_not_throw():
    test_data = get_html_data(Path('tests', 'integration', 'html_parser', 'test_html', 'w3schools.html'))
    test_ignored_tags = {"script", "style", "meta"}
    test_entity_name_separators = ["&nbsp;", "&lt;", "&gt;", "&amp;"]
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=lambda: create(WordBuilderPolicy.ENGLISH_WORD_POLICY),
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()

    assert result
    