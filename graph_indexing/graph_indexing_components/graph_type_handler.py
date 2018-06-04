class GraphTypeHandler:

    inner = None
    cache = None
    name_cache = None

    types = {"entity": 0,
             "event": 1,
             "literal": 2}

    def __init__(self, inner, type_cache, name_cache):
        self.inner = inner
        self.cache = type_cache
        self.name_cache = name_cache

    def process(self, triple):
        triple[0] = self.process_element(triple[0])
        triple[2] = self.process_element(triple[2])

        return self.inner.process(triple)

    def process_element(self, element):
        if element.endswith("@en"):
            element = element[:-3]
            self.cache.add(element, self.types["literal"])
            return element
        elif "^^" in element:
            element = element.split("^^")[0]
            self.cache.add(element, self.types["literal"])
            return element
        elif self.name_cache.contains(element):
            self.cache.add(element, self.types["entity"])
            return element
        else:
            self.cache.add(element, self.types["event"])
            return element