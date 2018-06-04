class GraphNameHandler:

    inner = None
    should_index = None
    name_relation = None

    def __init__(self, inner, name_relation, name_index, index=False):
        self.inner = inner
        self.should_index = index
        self.name_relation = name_relation
        self.name_index = name_index

    def process(self, triple):
        if self.should_index and triple[1] == self.name_relation:
            entity = triple[0]
            name = triple[2]

            self.name_index.add(entity, name)
        elif self.should_index:
            pass
        elif triple[1] == self.name_relation:
            pass
        else:
            subject_name = self.name_index.get(triple[0])
            object_name = self.name_index.get(triple[2])

            if subject_name is not None:
                triple[0] = subject_name

            if object_name is not None:
                triple[2] = object_name

            return self.inner.process(triple)