#!/usr/bin/python3
"""0. Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """  class BasicCache that inherits from BaseCaching
    and is a caching system:
    """

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
