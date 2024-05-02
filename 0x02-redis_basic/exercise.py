#!/usr/bin/env python3
""" Defines a module with a class Cache"""


import redis
import uuid
import sys
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """returns a Callable."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increments the count for key every time the method
           is called and returns the value returned by the original
           method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """returns a Callable."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ add its input parameters to one list in redis, and
            store its output into another list
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, *args)
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_key, res)
        return res
    return wrapper


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

    @count_calls
    @call_history
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


def replay(method: Callable) -> str:
    """display the history of calls of a particular function."""
    r = method.__self__
    print(dir(method), r)
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    key = f"{method.__qualname__}"

    count = f"Cache.store was called {int(r.get(key))} times:\n"
    input_lst = [element.decode('utf-8')
                 for element in r._redis.lrange(input_key, 0, -1)]
    output_lst = [element.decode('utf-8')
                  for element in r._redis.lrange(output_key, 0, -1)]

    return (count +
            "\n".join("Cache.store(*({},)) -> {}".format(str(inpt),
                                                         str(outpt))
                      for inpt, outpt in zip(input_lst, output_lst)))


if __name__ == "__main__":
    cache = Cache()

    # TEST_CASES = {
    #     b"foo": None,
    #     123: int,
    #     "name": str,
    #     "bar": lambda d: d.decode("utf-8")
    # }

    # for value, fn in TEST_CASES.items():
    #     key = cache.store(value)
    #     assert cache.get(key, fn=fn) == value
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    print(replay(cache.store))
