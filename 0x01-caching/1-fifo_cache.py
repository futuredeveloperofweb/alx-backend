#!/usr/bin/env python3
"""Module for task 1 that Create a class FIFOCache that inherits
from BaseCaching and is a caching system"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a cashing system"""
    def __init__(self):
        """methode used to intialize the cashing system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add items to the cashing system"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """retrieve the the items"""
        return self.cache_data.get(key, None)
