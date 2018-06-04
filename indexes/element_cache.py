from diskcache import Cache
import numpy as np

class ElementCache:

    map = None

    def __init__(self, path):
        self.map = Cache(path, size_limit=2 ** 42)

    def add(self, key, element):
        self.map[key] = element

    def get(self, element):
        if element not in self.map:
            return None

        return self.map[element]

    def contains(self, key):
        return key in self.map

    def count_elements(self):
        return len(self.map)

    def update(self, key, element):
        self.map[key] = element

    def index_keys(self, index):
        keys = list(self.map.iterkeys())
        for key in keys:
            value = self.map[key]
            key_index = index.to_index(key)

            if key_index > 0:
                self.map[key_index] = value

            del self.map[key]
