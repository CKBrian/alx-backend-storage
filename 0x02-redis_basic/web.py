#!/usr/bin/env python3
""" Defines a module with a class Cache"""


import redis
from typing import Union, Callable, Optional
from functools import wraps
import requests
import time


r = redis.Redis()
r.flushdb()


def get_url_count(method: Callable) -> Callable:
    """Returns a method that track access count, and
       cache the result.of a requested url"""
    @wraps(method)
    def wrapper(url):
        """returns url access count and cache url results"""
        cache_key = f"cache:{url}"

        response = requests.get(url)
        content = response.text
        print(content)

        r.setex(cache_key, 10, str(content))
        return method(url)

    return wrapper


@get_url_count
def get_page(url: str) -> str:
    """Obtain the HTML content of a URL, """
    key = f"count:{url}"
    cache_key = f"cache:{url}"
    r.incr(key)
    resp = requests.get(url)
    return str(resp)


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    for _ in range(5):
        print(get_page(url))
