import pytest
from unittest.mock import patch, MagicMock, AsyncMock
from typing import Any

from httpx import Response, Request

from myhttp.page import get_html_page, get_html_pages, is_response_valid


@pytest.mark.parametrize('response, expected',
                         [(Response(status_code=404, request=MagicMock()), False),
                          (Response(status_code=200, default_encoding='unsupported', request=MagicMock()), False),
                          (Response(status_code=200, headers={'content-type': 'application/json'}, request=MagicMock()), False),
                          (Response(status_code=200, default_encoding='utf-8', headers={'content-type': 'text/html other...'}, request=MagicMock()), True)],
                         ids=['invalid status code', 'invalid_encoding', 'invalid_content_type', 'valid'])
def test_is_response_valid(response, expected):
    assert is_response_valid(response) is expected


@patch('myhttp.page.is_response_valid', MagicMock(side_effect=[True, True]))
@patch('myhttp.page.get_responses')
def test_get_html_pages(get_responses_mock: AsyncMock):
    test_urls = ['https://test.com', 'https://test2.com']
    text_1, text_2  = 'dummy1', 'dummy2'
    get_responses_mock.return_value = [Response(status_code=200, text=text_1, request=Request(url=test_urls[0], method='GET')),
                                       Response(status_code=200, text=text_2, request=Request(url=test_urls[1], method='GET'))]
    
    result = get_html_pages(test_urls)

    assert result[test_urls[0]] == text_1
    assert result[test_urls[1]] == text_2


@patch('myhttp.page.is_response_valid', MagicMock(side_effect=[False, False]))
@patch('myhttp.page.get_responses')
def test_get_html_pages_invalid(get_responses_mock: AsyncMock):
    test_urls = ['https://test.com', 'https://test2.com']
    text_1, text_2  = 'dummy1', 'dummy2'
    get_responses_mock.return_value = [Response(status_code=501, request=Request(url=test_urls[0], method='GET')),
                                       Response(status_code=404, request=Request(url=test_urls[1], method='GET'))]
    
    result = get_html_pages(test_urls)

    assert result[test_urls[0]] is None
    assert result[test_urls[1]] is None


@patch('myhttp.page.get_html_pages', MagicMock(return_value = {'https://test.com': 'dummy_data'}))
def test_get_html_page():
    assert get_html_page('https://test.com') == 'dummy_data'


@patch('myhttp.page.get_html_pages', MagicMock(return_value = {}))
def test_get_html_page_invalid():
    with pytest.raises(Exception) as ex_info:
        get_html_page('https://test.com')
    
    assert isinstance(ex_info.value, RuntimeError)