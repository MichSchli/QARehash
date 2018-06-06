from example_readers.example_reader import ExampleReader
from example_readers.question_reader.question_reader_factory import QuestionReaderFactory
from experiment.interfaces.abstract_factory import AbstractFactory


class ExampleReaderFactory(AbstractFactory):

    def __init__(self):
        self.question_reader_factory = QuestionReaderFactory(None)

    def get(self, configuration):
        example_reader = ExampleReader()
        question_reader = self.question_reader_factory.get(configuration)
        example_reader.add_item_reader("question", question_reader)
        return example_reader