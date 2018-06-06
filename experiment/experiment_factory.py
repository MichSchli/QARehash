from experiment.experiment import Experiment
from experiment.interfaces.abstract_factory import AbstractFactory
from experiment.model_tester.model_tester_factory import ModelTesterFactory
from experiment.model_trainer.model_trainer_factory import ModelTrainerFactory


class ExperimentFactory(AbstractFactory):

    def __init__(self, model_factory, example_reader_factory, evaluator_factory):
        self.model_trainer_factory = ModelTrainerFactory(example_reader_factory, evaluator_factory)
        self.model_tester_factory = ModelTesterFactory(example_reader_factory)
        self.model_factory = model_factory
        self.example_reader_factory = example_reader_factory

    def get(self, configuration):
        experiment = Experiment()
        experiment.model_trainer = self.model_trainer_factory.get(configuration)
        experiment.model_tester = self.model_tester_factory.get(configuration)
        experiment.model = self.model_factory.get(configuration)

        return experiment