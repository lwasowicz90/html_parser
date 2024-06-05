"""
Script to display th page, extract words from html page, count it and present top 10 records
"""

from config import CONFIG
from logger import init as init_logger
from myhttp.page import get_html_page
from html_parser.parser import HtmlParser
from word.builder_factory import create as create_word_builder, WordBuilderPolicy



def main():
    init_logger()
    html_data = get_html_page(CONFIG.url)
    print(html_data)

if __name__ == '__main__':    
    main()
    # html_text = open('./data/w3schools.html', 'r', encoding='utf-8').read()
    # parser = HtmlParser(html_data=html_text,
    #                     create_word_builder=lambda: create_word_builder(
    #                         WordBuilderPolicy.ENGLISH_WORD_POLICY),
    #                     tags_ignored=CONFIG.tags_ignored,
    #                     entity_name_separators=CONFIG.html_entity_name_separators)
    # result = list(parser.get_all_words())
    # print(result)
    # with open('data/result.json', 'w') as file:
    #     import json
    #     json.dump(result, file)
