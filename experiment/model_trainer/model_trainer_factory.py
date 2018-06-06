from experiment.interfaces.abstract_factory import AbstractFactory
from experiment.model_trainer.model_trainer import ModelTrainer


class ModelTrainerFactory(AbstractFactory):

    def __init__(self, example_reader_factory, evaluator_factory):
        self.example_reader_factory = example_reader_factory
        self.evaluator_factory = evaluator_factory

    def get(self, configuration):
        model_trainer = ModelTrainer()

        model_trainer.iterations = configuration["training"]["iterations"]
        model_trainer.train_example_reader = self.example_reader_factory.get(configuration)
        model_trainer.periodic_tests = configuration["training"]["periodic_tests"] if "periodic_tests" in configuration["training"] else None

        if model_trainer.periodic_tests is not None:
            model_trainer.validation_example_reader = self.evaluator_factory.get(configuration)

        return model_trainer