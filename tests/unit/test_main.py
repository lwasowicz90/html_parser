from unittest.mock import patch, MagicMock, ANY

from main import main as uut


@patch('main.CONFIG', MagicMock(**{'url': 'dummy_url', 'tags_ignored': 'dummy_tags', 'html_entity_name_separators': 'dummy_entities'}))
@patch('main.get_html_page', MagicMock(return_value = 'dummy_page'))
@patch('main.save_to_file')
@patch('main.get_top_n_occurences')
@patch('main.HtmlParser')
@patch('main.open_page_in_browser')
@patch('main.init_logger')
def test_main(init_logger_mock: MagicMock,
              open_page_in_browser_mock: MagicMock,
              parser_mock: MagicMock,
              get_top_n_occurences_mock: MagicMock,
              save_to_file_mock: MagicMock
              ):
    dummy_words = ['test', 'word']
    parser_instance_mock = MagicMock()
    parser_mock.return_value = parser_instance_mock
    parser_instance_mock.get_all_words.return_value = dummy_words
    test_occurences = 22
    get_top_n_occurences_mock.return_value = test_occurences
    
    uut()

    init_logger_mock.assert_called_once()
    open_page_in_browser_mock.assert_called_once_with('dummy_url')
    parser_mock.assert_called_once_with('dummy_page',
                                        create_word_builder=ANY,
                                        tags_ignored='dummy_tags',
                                        entity_name_separators='dummy_entities')
    get_top_n_occurences_mock.assert_called_once_with(dummy_words, 10)
    save_to_file_mock.assert_called_once_with(test_occurences)