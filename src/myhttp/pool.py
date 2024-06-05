"""Pool for http requests
"""
import asyncio

import httpx


async def get_responses(urls: list[str]) -> list[httpx.Response]:
    """
        For simplicity it sends all requests at once.
        It is good practice to throttle requests and send in batches, especially
        if sent to the same server
    :param urls: 
    :return: responses
    """
    client = httpx.AsyncClient()
    tasks = [client.get(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return responses
