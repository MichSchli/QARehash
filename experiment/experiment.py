class Experiment:

    def run(self):
        self.model.initialize()

        self.model_trainer.train(self.model)
        self.model_tester.test(self.model)