class ModelTrainer:

    iterations = None
    periodic_tests = None

    validation_example_reader = None
    training_example_reader = None

    def __init__(self):
        pass

    def train(self, model):
        for iteration in range(self.iterations):
            for example in self.train_example_reader.iterate("train"):
                model.update(example)

            if self.periodic_tests is not None and iteration % self.periodic_tests == 0 and iteration > 0:
                self.validation_evaluator.evaluate(model)