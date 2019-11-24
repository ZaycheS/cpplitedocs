from description import Description


class EnumMember(Description):
    name = ''

    def __init__(self, type='', name=''):
        self.type = type
        self.name = name
        self.keywords = list()

    def __str__(self):
        string = self.name
        if self.get_brief_desc() != '':
            string += '\nBrief:' + self.get_brief_desc()
        if self.get_detailed_desc() != '':
            string += '\nDetailed:' + self.get_detailed_desc() + '\t'
        return string

    def set_name(self, name):
        self.name = name
