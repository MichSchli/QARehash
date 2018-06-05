class GraphNameHandler:

    inner = None
    should_index = None
    name_relation = None

    def __init__(self, inner, name_relation, name_index, discarded_name_file, index=False):
        self.inner = inner
        self.should_index = index
        self.name_relation = name_relation
        self.name_index = name_index

        self.discarded_names = self.get_discarded_names(discarded_name_file)

    def get_discarded_names(self, discarded_name_file):
        if discarded_name_file == "none":
            return []
        else:
            discarded_names = []
            for line in open(discarded_name_file):
                discarded_names.append(line.strip())
            return discarded_names

    def process(self, triple):
        if self.should_index and triple[1] == self.name_relation:
            entity = triple[0]
            name = triple[2]

            if name.endswith("@en"):
                name = name[:-3]

            if name in self.discarded_names:
                return

            self.name_index.add(entity, name)
        elif self.should_index:
            pass
        elif triple[1] == self.name_relation:
            pass
        else:
            #subject_name = self.name_index.get(triple[0])
            #object_name = self.name_index.get(triple[2])

            #if subject_name is not None:
            #    triple[0] = subject_name

            #if object_name is not None:
            #    triple[2] = object_name

            return self.inner.process(triple)