from experiment.interfaces.abstract_factory import AbstractFactory
from experiment.model_tester.model_tester import ModelTester


class ModelTesterFactory(AbstractFactory):

    def __init__(self, example_reader_factory):
        self.example_reader_factory = example_reader_factory

    def get(self, configuration):
        return ModelTester()