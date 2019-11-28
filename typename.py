from description import Description
from util import *

class TypeName(Description):
    type = ''
    name = ''

    def __init__(self, type='', name=''):
        self.set_detailed_desc("Here must be description, but here isn't")
        self.type = type
        self.name = name
        self.keywords = list()

    def generate_name(self):
        name = "Attribute "
        name += "<a href=#" + self.name + " >" +self.type+" "+ self.name + "</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"

    def generate_card(self, parent_name=None):
        card = ''
        card += card1
        card += "<a " + "id=" + self.name + "></a>"
        card += "Attribute "
        card += self.type+" "+self.name if self.name != "DEFAULT" else ""
        card += card2
        card += str(self.get_detailed_desc())
        card += card3
        if parent_name is not None:
            card += card4 + " " + parent_name
        card += card5
        return card
    def __str__(self):
        string = ''
        if self.type != '':
            string = self.type + ":"
        else:
            string = ''
        string += self.name
        if len(self.keywords) > 0:
            string += '\nKeywords:' + ' '.join(
                map(str, self.keywords))
        if self.get_brief_desc() != '':
            string += '\nBrief:' + self.get_brief_desc()
        if self.get_detailed_desc() != '':
            string += '\nDetailed:' + self.get_detailed_desc()+'\t'
        return string

    def set_name(self, name):
        self.name = name

    def set_type(self, type):
        self.type = type

