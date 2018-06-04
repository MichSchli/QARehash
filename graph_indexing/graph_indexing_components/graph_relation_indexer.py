class GraphRelationIndexer:

    def __init__(self, inner, index):
        self.inner = inner
        self.index = index

    def process(self, triple):
        triple[1] = str(self.index.add(triple[1]))
        return self.inner.process(triple)