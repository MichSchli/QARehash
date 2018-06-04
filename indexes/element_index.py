from diskcache import Cache
import numpy as np

from indexes.element_cache import ElementCache


class ElementIndex:

    forward_map = None
    backward_map = None
    vectors = None

    def __init__(self, path):
        self.forward_map = ElementCache(path + ".forward")
        self.backward_map = ElementCache(path + ".backward")
        self.element_counter = self.forward_map.count_elements()
        self.add("<unknown>")

    def add(self, element):
        if self.forward_map.contains(element):
            return self.forward_map.get(element)

        key = self.element_counter
        self.forward_map.add(element, key)
        self.backward_map.add(key, element)
        self.element_counter += 1

        return self.element_counter - 1

    def to_index(self, key):
        index = self.forward_map.get(key)
        if index is None:
            return 0
        else:
            return index

    def from_index(self, key):
        key = int(key)

        if key >= self.element_counter:
            return None

        return self.backward_map.get(key)