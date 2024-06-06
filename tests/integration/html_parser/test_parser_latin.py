from pathlib import Path

from word.builder_factory import create, WordBuilderPolicy
from html_parser.parser import HtmlParser


def get_html_data(filepath: Path) -> str:
    with open(filepath, 'r', encoding='utf-8') as test_file:
        return test_file.read()


def test_parsing_german():
    test_data = get_html_data(Path('tests', 'integration', 'html_parser', 'test_html', 'german.html'))
    test_ignored_tags = {"script", "style", "meta"}
    test_entity_name_separators = ["&nbsp;", "&lt;", "&gt;", "&amp;", "&quot;"]
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=lambda: create(WordBuilderPolicy.LATIN_LANGUAGE_POLICY),
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()

    assert result == ('In', 'seiner', 'Regierungserklärung', 'macht', 'der', 'Kanzler', 'deutlich', 'Die', 'Abschiebung',
                       'von', 'Schwerstkriminellen', 'nach', 'Afghanistan', 'und', 'Syrien', 'soll', 'wieder', 'möglich',
                       'werden', 'Während', 'CDU', 'Chef', 'Merz', 'zum', 'raschen', 'Handeln', 'drängt', 'sind', 'die', 
                       'Grünen', 'skeptisch')


def test_parsing_polish():
    test_data = get_html_data(Path('tests', 'integration', 'html_parser', 'test_html', 'polish.html'))
    test_ignored_tags = {"script", "style", "meta"}
    test_entity_name_separators = ["&nbsp;", "&lt;", "&gt;", "&amp;", "&quot;"]
    uut = HtmlParser(html_data=test_data,
                     create_word_builder=lambda: create(WordBuilderPolicy.LATIN_LANGUAGE_POLICY),
                     tags_ignored=test_ignored_tags,
                     entity_name_separators=test_entity_name_separators)
    
    result = uut.get_all_words()

    assert result == ('Bulwersujące', 'w', 'jaki', 'sposób', 'doszło', 'do', 'zatrzymania', 'żołnierzy', 'zważywszy',
                      'też', 'na', 'to', 'że', 'w', 'ostatnim', 'czasie', 'nasi', 'żołnierze', 'przy', 'granicy', 
                      'zostali', 'zaatakowani', 'powiedział', 'prezydent', 'Andrzej', 'Duda', 'reagując', 'na', 
                      'zatrzymanie', 'polskich', 'żołnierzy', 'na', 'granicy', 'z', 'Białorusią')
