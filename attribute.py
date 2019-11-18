class Attribute:
    type = ''
    name = ''
    keywords = []

    def __init__(self, type='', name=''):
        self.type = type
        self.name = name

    def __str__(self):
        return self.type + ':' + self.name

    def add_keyword(self, keyword):
        self.keywords.append(keyword)

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type
