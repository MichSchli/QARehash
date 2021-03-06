class Question:

    words = None
    pos = None
    dep_heads = None
    dep_types = None

    word_indexes = None
    pos_indexes = None

    def count_words(self):
        return self.word_indexes.shape[0]

    def get_word_indexes(self):
        return self.word_indexes

    def get_pos_indexes(self):
        return self.pos_indexes

    def __str__(self):
        return " ".join(self.words)