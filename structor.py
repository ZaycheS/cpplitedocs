from description import Description
from util import *

class StructorDesc(Description):
    name = ''
    type = bool()  # True-constructor False -destructor
    parameters = list()

    def generate_name(self):
        name = "Constructor " if self.type else "Destructor "
        name += "<a href=#" + self.name + " >" + self.name + "</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"

    def generate_card(self, parent_name=None):
        card = ''
        card += card1
        card += "Constructor " if self.type else "Destructor "
        card += "<a " + "id=" + self.name + "></a>"
        card += self.name if self.name != "DEFAULT" else ""
        card += card2
        card += str(self.get_detailed_desc())
        if len(self.keywords) > 0:
            card += card2_q
            for i in self.keywords:
                card += i + "&nbsp"
        if len(self.parameters) > 0:
            card += card3_2
            for i in self.parameters:
                if i.name is not None and i.name != "DEFAULT":
                    card += i.type+" "+i.name + "<br>"
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card
    def __str__(self):
        string = 'STRUCTOR OF ' + self.name + ' type:'
        if self.type:
            string += ' constructor'
        else:
            string += ' destructor'
        string += ' attributes:' + ' '.join(
            map(str, self.parameters)) + '\nKeywords:' + ' '.join(
            map(str,
                self.keywords)) + '\nBrief description:' + self.get_brief_desc() + '\nDetailed desription:\n' + self.get_detailed_desc() + '\n'
        return string

    def __init__(self):
        self.set_detailed_desc("Here must be description, but here isn't")
        self.parameters = list()
        self.keywords = list()

    def add_parameter(self, attribute):
        self.parameters.append(attribute)
