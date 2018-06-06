from example_readers.question_reader.question import Question


class QuestionReader:

    def __init__(self, dataset_map):
        self.datasets = {}
        self.dataset_map = dataset_map

    def build(self, array_question):
        question = Question()
        question.words = [array_question[j][1] for j in range(len(array_question))]
        question.pos = [array_question[j][3] for j in range(len(array_question))]
        question.dep_types = [array_question[j][4] for j in range(len(array_question))]
        question.dep_heads = [int(array_question[j][5]) for j in range(len(array_question))]

        return question

    def read(self, index, dataset):
        if dataset not in self.datasets:
            self.load_data(dataset)

        return self.build(self.datasets[dataset][index])

    def load_data(self, dataset):
        f = open(self.dataset_map[dataset], 'r')
        for line in f:
            print(line)