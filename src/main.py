"""
Script to display th page, extract words from html page, count it and present top 10 records
"""

import logging
import sys

from browser import open_page as open_page_in_browser
from calc.word import get_top_n_occurences
from config import CONFIG
from file.save import save_to_file
from logger import init as init_logger
from myhttp.page import get_html_page
from html_parser.parser import HtmlParser
from word.builder_factory import create as create_word_builder, WordBuilderPolicy


def main():
    """main function of the script
    """
    init_logger()
    open_page_in_browser(CONFIG.url)
    html_data = get_html_page(CONFIG.url)
    parser = HtmlParser(html_data,
                        create_word_builder=lambda: create_word_builder(WordBuilderPolicy.ENGLISH_WORD_POLICY),
                        tags_ignored=CONFIG.tags_ignored,
                        entity_name_separators=CONFIG.html_entity_name_separators
                        )
    words = parser.get_all_words()
    word_occurences = get_top_n_occurences(words, 10)
    save_to_file(word_occurences)


if __name__ == '__main__':
    try:
        main()
    except Exception:
        logging.getLogger('main').error("Failed executing the script", exc_info=True)
        sys.exit(-1)
    sys.exit(0)
