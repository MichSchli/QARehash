from example_readers.example_reader_factory import ExampleReaderFactory
from experiment.experiment_factory import ExperimentFactory
from experiment.interfaces.abstract_example_reader import AbstractExampleReader
from experiment.interfaces.abstract_factory import AbstractFactory


class DummyModel:

    def initialize(self):
        pass

    def update(self, example):
        print(example)

class DummyModelFactory:

    def get(self, configuration):
        return DummyModel()

model_configuration = "/home/michael/Projects/QuestionAnswering/GCNQA3/configurations/models/webquestions_relation_prediction.cfg"

configuration = {"training": {"iterations": 5}}

experiment_factory = ExperimentFactory(DummyModelFactory(), ExampleReaderFactory(), AbstractFactory())
experiment = experiment_factory.get(configuration)
experiment.run()