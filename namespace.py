from description import *
from typename import TypeName
from util import *


class NamespaceDesc(Description):
    name = ' '
    descs_list = list()

    def generate_name(self):
        name = "Namescpace "
        name += "<a href=#"+self.name+" >"+self.name+"</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + "<pre>" + self.get_brief_desc()+"</pre>"
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"

    def generate_card(self, parent_name):
        card = ''
        card += card1
        card += "<a " + "id=" + self.name + "></a>"
        card += "Namespace "
        card += self.name if self.name != "DEFAULT" else ""
        card += card2
        card += "<pre>"+str(self.get_detailed_desc())+"</pre>"
        if len(self.keywords) > 0:
            card += card2_q
            for i in self.keywords:
                card += i + "&nbsp"
        if len(self.descs_list) > 0:
            card += card3
            for i in self.descs_list:
                if i.name is not None and i.name != "DEFAULT":
                    card += "-" + i.name + "<br>"
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card

    def __init__(self):
        self.name = ''
        self.descs_list = list()
        self.keywords = list()
        self.parent = TypeName()
        self.set_detailed_desc("Here must be description, but here isn't")

    def __str__(self):
        string = "Namespace name:" + self.name
        string += '\n ReLATEd:' + '\n'.join(map(str, self.descs_list)) + '\nEND OF RELATED' + '\n'
        return string

    def set_name(self, name):
        self.name = name
