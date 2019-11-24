from description import *
from typename import TypeName


class ClassDesc(Description):
    name = ' '
    descs_list = list()
    parent = list()

    def __init__(self):
        self.name = ''
        self.descs_list = list()
        self.keywords = list()
        self.parent = list()

    def __str__(self):
        string = "Class name:" + self.name
        if str(self.parent) != '':
            string += "\nParent:" + '\n'.join(map(str, self.parent))
        string += '\n ReLATEd:' + '\n'.join(map(str, self.descs_list)) + '\nEND OF RELATED' + '\n'
        return string

    def set_name(self, name):
        self.name = name

    def add_parent(self, parent):
        self.parent.append(parent)

    def set_parent(self, parent):
        self.parent = parent
