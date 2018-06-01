class GraphRelationIndexer:

    def __init__(self, inner):
        self.inner = inner

    def process(self, triple):
        return self.inner.process(triple)