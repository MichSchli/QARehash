class GraphRelationFilter:

    def __init__(self, inner, discarded_relation_file, name_relation):
        self.inner = inner
        self.removed = self.get_discarded_relations(discarded_relation_file)
        self.removed.append(name_relation)

    def get_discarded_relations(self, discarded_relation_file):
        if discarded_relation_file == "none":
            return []
        else:
            discarded_relations = []
            for line in open(discarded_relation_file):
                discarded_relations.append(line.strip())
            return discarded_relations

    def process(self, triple):
        if triple[1] in self.removed:
            return None
        return self.inner.process(triple)