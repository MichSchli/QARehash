class GraphFileIterator:

    def __init__(self, filename, separator="\t"):
        self.filename = filename
        self.separator = separator

    def iterate(self):
        for line in open(self.filename):
            line = line.strip().split(self.separator)
            yield line