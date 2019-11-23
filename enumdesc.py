class EnumDesc:
    name = ' '
    enumers = list()

    def __init__(self):
        self.enumers = list()

    def __str__(self):
        return "\nEnumeration name:" + self.name + "\nEnumers:\n" + ' '.join(map(str, self.enumers))

    def set_name(self, name):
        self.name = name
