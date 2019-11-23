from description import Description


class TypeName(Description):
    type = ''
    name = ''

    def __init__(self, type='', name=''):
        self.type = type
        self.name = name
        self.keywords = list()

    def __str__(self):
        string = ''
        if self.type != '':
            string = self.type + ":"
        else:
            string = ''
        string += self.name
        if len(self.keywords) > 0:
            string += '\nKeywords:' + ' '.join(
                map(str, self.keywords))
        if self.get_brief_desc() != '':
            string += '\nBrief:' + self.get_brief_desc()
        if self.get_detailed_desc() != '':
            string += '\nDetailed:' + self.get_detailed_desc()
        return string

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

