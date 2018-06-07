from example_readers.example import Example
from experiment.interfaces.abstract_example_reader import AbstractExampleReader


class ExampleReader(AbstractExampleReader):

    item_readers = None
    dataset_lengths = None

    def __init__(self):
        self.item_readers = {}
        self.dataset_lengths = {}

    def add_item_reader(self, key, item_reader):
        self.item_readers[key] = item_reader

    def get_dataset_size(self, dataset):
        if dataset in self.dataset_lengths:
            return self.dataset_lengths[dataset]

        size = None
        for item_reader in self.item_readers.values():
            item_reader_dataset_size = item_reader.get_dataset_size(dataset)
            if size is None:
                size = item_reader_dataset_size
            elif size != item_reader_dataset_size:
                print("ERROR")
                exit()

        self.dataset_lengths[dataset] = size
        return size


    def iterate(self, dataset):
        size = self.get_dataset_size(dataset)

        for index in range(size):
            example = Example()
            for key, item_reader in self.item_readers.items():
                item = item_reader.read(index, dataset)
                example.add_item(key, item)
            yield example