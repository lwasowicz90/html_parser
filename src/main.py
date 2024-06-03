"""
Script to display th page, extract words from html page, count it and present top 10 records
"""

from config import CONFIG
from logger import init as init_logger
from html_parser.parser import HtmlParser
from word.builder_factory import create as create_word_builder, WordBuilderPolicy


if __name__ == '__main__':    
    init_logger()    
    html_text = open('./data/w3schools.html', 'r', encoding='utf-8').read()
    parser = HtmlParser(html_data=html_text,
                        create_word_builder=lambda: create_word_builder(
                            WordBuilderPolicy.ENGLISH_WORD_POLICY),
                        tags_ignored=CONFIG.tags_ignored,
                        entity_name_separators=CONFIG.html_entity_name_separators)
    result = list(parser.get_all_words())
    print(result)
    with open('data/result.json', 'w') as file:
        import json
        json.dump(result, file)
