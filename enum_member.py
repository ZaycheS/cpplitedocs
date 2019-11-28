from description import Description
from util import *


class EnumMember(Description):
    name = ''

    def generate_name(self):
        name = "<a href=#" + self.name + " >" + self.name + "</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"



    def __init__(self, type='', name=''):
        self.set_detailed_desc("Here must be description, but here isn't")
        self.type = type
        self.name = name
        self.keywords = list()

    def generate_card(self, parent_name=None):
        card = ''
        card += card1
        card += "<a " + "id=" + self.name + "></a>"
        card += "Enumeration member "
        card += self.name if self.name != "DEFAULT" else ""
        card += card2
        card += str(self.get_detailed_desc())
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card

    def __str__(self):
        string = self.name
        if self.get_brief_desc() != '':
            string += '\nBrief:' + self.get_brief_desc()
        if self.get_detailed_desc() != '':
            string += '\nDetailed:' + self.get_detailed_desc() + '\t'
        return string

    def set_name(self, name):
        self.name = name
