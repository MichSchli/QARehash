from example_readers.example import Example
from experiment.interfaces.abstract_example_reader import AbstractExampleReader


class ExampleReader(AbstractExampleReader):

    item_readers = None

    def __init__(self):
        self.item_readers = {}

    def add_item_reader(self, key, item_reader):
        self.item_readers[key] = item_reader

    def iterate(self, dataset):
        index = 0
        example = Example()
        for key, item_reader in self.item_readers.items():
            item = item_reader.read(index, dataset)
            example.add_item(key, item)
        yield example