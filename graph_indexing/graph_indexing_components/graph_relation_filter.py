class GraphRelationFilter:

    removed = ["http://rdf.freebase.com/ns/type.object.name"]

    def __init__(self, inner):
        self.inner = inner

    def process(self, triple):
        if triple[1] in self.removed:
            return None
        return self.inner.process(triple)