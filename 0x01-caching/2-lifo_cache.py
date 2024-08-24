#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """init method"""
        self.last_put = ""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_put)
            print("DISCARD:", self.last_put)

        if key:
            self.last_put = key

    def get(self, key):
        """Must return the value in self.cache_data linked to key."""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
