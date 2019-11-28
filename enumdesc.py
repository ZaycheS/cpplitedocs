from util import *
from description import Description


class EnumDesc(Description):
    name = ' '
    descs_list = list()

    def __init__(self):
        self.set_detailed_desc("Here must be description, but here isn't")
        self.descs_list = list()

    def generate_name(self):
        name = "Enumeration "
        name += "<a href=#"+self.name+" >"+self.name+"</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"

    def __str__(self):
        return "\nEnumeration name:" + self.name + "\nEnumers:\n" + '\n'.join(map(str, self.descs_list)) + '\n'

    def generate_card(self, parent_name=None):
        card = ''
        card += card1
        card += "<a "+"id="+self.name+"></a>Enumeration "
        card += self.name if self.name != "DEFAULT" else ""
        card += card2
        card += str(self.get_detailed_desc())
        if len(self.keywords) > 0:
            card += card2_q
            for i in self.keywords:
                card += i + "&nbsp"
        if len(self.descs_list) > 0:
            card += card3
            for i in self.descs_list:
                if i.name is not None and i.name != "DEFAULT":
                    card +=i.name + "<br>"
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card

    def set_name(self, name):
        self.name = name
