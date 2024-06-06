"""Extracts html page from http response
"""
import asyncio
import logging

from httpx import Response

from myhttp.pool import get_responses


SUPPORTED_ENCODING = ['utf-8']
SUPPORTED_CONTENT_TYPE = 'text/html'
logger = logging.getLogger('html_page')


def is_response_valid(response: Response) -> bool:
    """Checks if response is valid

    :param response:
    :return: True if response code 200 and supported encoding, False otherwise
    """
    if response.status_code != 200:
        logger.error('Invalid status code (%d) for %s!', response.status_code, response.request.url)
        return False
    if not response.encoding in SUPPORTED_ENCODING:
        logger.error('Invalid encoding, it supports %s right now!', str(SUPPORTED_ENCODING))
        return False
    if not SUPPORTED_CONTENT_TYPE in response.headers['content-type']:
        logger.error('Invalid content-type: %s, it supports only %s', response.headers['content-type'], SUPPORTED_CONTENT_TYPE)
        return False
    return True


def get_html_pages(urls: list[str]) -> dict:
    """Reads content of html pages
    :param urls: 
    :return: dict with url: html page
    """
    responses = asyncio.run(get_responses(urls))
    return {response.request.url: response.text if is_response_valid(response) else None for response in responses}


def get_html_page(url: str) -> str:
    """Reads html page from web
    :param url:
    :raises RuntimeError: when page can not be read
    :return: html page in string
    """
    pages = get_html_pages([url])
    if url not in pages:
        raise RuntimeError('Cannot read the page {url}')
    return pages[url]
