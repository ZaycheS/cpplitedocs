from description import *
from typename import TypeName
from util import *


class ClassDesc(Description):
    name = ' '
    descs_list = list()
    parents = list()
    type = True  # True-Class False-Struct

    def generate_name(self):
        name = "Class " if self.type else "Structure "
        name += "<a href=#" + self.name + " >" + self.name + "</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>"+name + "</p></li>\n"

    def __init__(self):
        self.set_detailed_desc("Here must be description, but here isn`t")
        self.name = ''
        self.descs_list = list()
        self.keywords = list()
        self.parents = list()

    def generate_card(self, parent_name):
        card = ''
        card += card1
        card += "<a " + "id=" + self.name + "></a>"
        card += "Class " if self.type else "Structure "
        card += self.name if self.name != "DEFAULT" else ""
        card += card2
        if self.get_detailed_desc()!='':
            card+=self.get_detailed_desc()
        if len(self.keywords) > 0:
            card += card2_q
            for i in self.keywords:
                card += i + "&nbsp"
        if len(self.parents) > 0:
            card += card2_5
            for i in self.parents:
                card += i.name + "<br>"

        if len(self.descs_list) > 0:
            card += card3
            for i in self.descs_list:
                if i.name is not None and i.name != "DEFAULT":
                    card += "-" + i.name + "<br>"
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card

    def __str__(self):
        string = "Class name:" + self.name
        if str(self.parents) != '':
            string += "\nParent:" + '\n'.join(map(str, self.parents))
        string += '\n ReLATEd:' + '\n'.join(map(str, self.descs_list)) + '\nEND OF RELATED' + '\n'
        return string

    def set_name(self, name):
        self.name = name

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_parent(self, parent):
        self.parents = parent
