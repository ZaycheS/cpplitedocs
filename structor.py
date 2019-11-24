from description import Description


class StructorDesc(Description):
    name = ''
    type = bool()  # True-constructor False -destructor
    attributes = list()

    def __str__(self):
        string='STRUCTOR OF ' + self.name + ' type:'
        if self.type:
            string+=' constructor'
        else:
            string+=' destructor'
        string+=' attributes:' + ' '.join(
            map(str, self.attributes)) + '\nKeywords:' + ' '.join(
            map(str,
                self.keywords)) + '\nBrief description:' + self.get_brief_desc() + '\nDetailed desription:\n' + self.get_detailed_desc()+'\n'
        return string

    def __init__(self):
        self.comment = "Here must be description, but here isn't"
        self.attributes = list()
        self.keywords = list()

    def add_parameter(self, attribute):
        self.attributes.append(attribute)
