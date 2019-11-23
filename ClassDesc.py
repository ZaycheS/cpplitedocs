from description import *
from typename import TypeName


class ClassDesc(Description):
    name = ' '
    descs_list = list()
    parent = TypeName()

    def __init__(self):
        self.name = ''
        self.descs_list = list()
        self.keywords = list()
        self.parent = TypeName()

    def __str__(self):
        string = "Class name:" + self.name
        if str(self.parent) != '':
            string += "\nParent:" + str(self.parent)
        string += '\n ReLATEd:' + '\n'.join(map(str, self.descs_list)) + '\nEND OF RELATED'
        return string

    def set_name(self, name):
        self.name = name

    def set_parent(self, parent):
        self.parent = parent
