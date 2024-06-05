from unittest.mock import patch, MagicMock

from browser.page import open_page as uut


@patch('browser.page.subprocess')
def test_open_page_default_browser(subprocess_mock: MagicMock):
    test_page = 'https://dummy.com'
    
    uut(test_page)

    subprocess_mock.call.assert_called_once_with(['open', '-a', 'Google Chrome', test_page])


@patch('browser.page.subprocess')
def test_open_page_custom_browser(subprocess_mock: MagicMock):
    test_page = 'https://dummy.com'
    test_browser = 'custom browser'
    
    uut(test_page, test_browser)

    subprocess_mock.call.assert_called_once_with(['open', '-a', test_browser, test_page])
