#!/usr/bin/env python3
""" Defines a module with a class Cache"""


import redis
import uuid
import sys
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initializes a redis Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str, fn: Optional[Callable] = None):
        """returns a string

            Args:
                key (str): a string
                fn (Optional[Callable]): function callable to convert
                                         the data back to the desired format.
            Return:
                  Nothing
        """
        val = self._redis.get(key)

        return fn(val) if fn else val

    def get_str(self):
        """parametrizes Cache.get with the string conversion function"""
        return self.decode("utf-8")


    def get_int(self):
        """parametrizes Cache.get with the int conversion function"""
        return int.from_bytes(self, sys.byteorder)


    def store(self, data: Union[int, float, str, bytes]) -> str:
        """returns a string

            Args:
                data (Union[int, float, str, bytes]): can be a str,
                      bytes, int or float.
            Return:
                  str: a key string of the stored data
        """
        r = self._redis
        key = str(uuid.uuid4())
        r.set(key, data)
        return key



if __name__ == "__main__":
    c = Cache()
    print(c.store("My Mother"))

    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "name": str,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
