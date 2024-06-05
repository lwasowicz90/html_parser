import pytest

from myhttp.pool import get_responses


@pytest.mark.asyncio
async def test_get_responses(httpx_mock):
    url_1, url_2 = 'https://test.com', 'https://test2.com'
    text_1, text_2  = 'dummy1', 'dummy2'
    httpx_mock.add_response(url_1, text=text_1)
    httpx_mock.add_response(url_2, text=text_2)

    responses = await get_responses([url_1, url_2])

    assert responses[0].request.url == url_1
    assert responses[0].text == text_1
    assert responses[1].request.url == url_2
    assert responses[1].text == text_2
