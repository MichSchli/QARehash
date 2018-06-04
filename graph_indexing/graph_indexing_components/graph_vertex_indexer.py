class GraphVertexIndexer:

    def __init__(self, inner, index):
        self.inner = inner
        self.index = index

    def process(self, triple):
        left = triple[0]
        right = triple[2]

        triple[0] = self.index_element(left)
        triple[2] = self.index_element(right)

        return self.inner.process(triple)

    def index_element(self, element):
        if element.endswith("@en"):
            element = element[:-3]
            return str(self.index.add(element)) + "@en"
        elif "^^" in element:
            parts = element.split("^^")
            element = parts[0]
            return str(self.index.add(element)) + "^^" + parts[1]
        else:
            return str(self.index.add(element))