class Example:

    items = None

    def __init__(self):
        self.items = {}

    def add_item(self, area, item):
        self.items[area] = item

    def __str__(self):
        string = "Example: { "

        for key, value in self.items:
            string += key + ": " + str(value)
            string += "\n"

        string += "}"

        return string