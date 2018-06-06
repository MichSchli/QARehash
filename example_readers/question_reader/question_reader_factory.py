from example_readers.question_reader.question_reader import QuestionReader


class QuestionReaderFactory:
    index_factory = None

    def __init__(self, index_factory):
        self.index_factory = index_factory

    def get(self, experiment_configuration):
        #word_index = self.index_factory.get("words", experiment_configuration)
        #pos_index = self.index_factory.get("pos", experiment_configuration)

        dataset_map = {"train": experiment_configuration["question_dataset"]["train"],
                       "valid": experiment_configuration["question_dataset"]["valid"],
                       "test": experiment_configuration["question_dataset"]["test"]}

        question_reader = QuestionReader()
        return question_reader