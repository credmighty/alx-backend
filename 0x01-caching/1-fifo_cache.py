#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """this class inherits from BaseCache"""
    def __init__(self):
        """Initialization methond"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return key

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_removed = self.key_indexes.pop(0)
                del self.cache_data[item_removed]
                print('DISCARD:', item_removed)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """Must return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
