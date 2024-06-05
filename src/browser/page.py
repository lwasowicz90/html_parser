"""opens page in browser
"""
import logging
import subprocess


DEFAULT_BROWSER_NAME = "Google Chrome"


def open_page(url: str, browser = DEFAULT_BROWSER_NAME):
    """Opens web page in browser
    :param url: _description_
    """
    logging.info('Opening %s in %s', url, browser)
    subprocess.call(['open', '-a', browser, url])
