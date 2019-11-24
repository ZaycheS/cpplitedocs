from description import *
from typename import TypeName


class NamespaceDesc(Description):
    name = ' '
    descs_list=list()

    def __init__(self):
        self.name = ''
        self.descs_list = list()
        self.keywords = list()
        self.parent = TypeName()

    def __str__(self):
        string = "Namespace name:" + self.name
        string+='\n ReLATEd:'+'\n'.join(map(str,self.descs_list))+'\nEND OF RELATED'+'\n'
        return string

    def set_name(self, name):
        self.name = name
