#!/usr/bin/env python3
"""LFU Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system"""
    def __init__(self) -> None:
        """init method"""
        self.temp_list = {}
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item"""

        if not (key is None or item is None):
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                pop = min(self.temp_list, key=self.temp_list.get)
                self.temp_list.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")
            if not (key in self.temp_list):
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

    def get(self, key):
        """
        Get an item by key
        """
        if (key is None) or not (key in self.cache_data):
            return None
        self.temp_list[key] += 1
        return self.cache_data.get(key)
