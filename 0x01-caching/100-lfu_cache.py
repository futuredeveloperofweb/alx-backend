#!/usr/bin/env python3
"""Module for task 5 that has LFUCashe class"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialize the cashing system"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def put(self, key, item):
        """mothode put adds new keys to the cash"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """get methode retrieve keys from the cash"""
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
