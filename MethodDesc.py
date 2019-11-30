from util import *
from description import Description
class MethodDesc(Description):
    name = ''
    type = ''
    parameters = list()

    def generate_name(self):
        name = "Method "
        name += "<a href=#" + self.name + " >" +self.type+" "+ self.name + "</a>"
        if self.get_brief_desc() != '':
            name += "<br>" + self.get_brief_desc()
        return "<li class=\"list-group-item\"><p>" + name + "</p></li>\n"

    def generate_card(self, parent_name=None):
        card = ''
        card += card1
        card += "<a " + "id=" + self.name + "></a>"
        card += "Function "
        card += self.type+" "+self.name if self.name != "DEFAULT" else ""
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
        return 'Description of ' + self.name + ' type:' + self.type + ' attributes:' + ' '.join(
            map(str, self.parameters)) + '\nKeywords:' + ' '.join(
            map(str,
                self.keywords)) + '\nBrief description:' + self.get_brief_desc() + '\nDetailed desсription:\n' \
               + self.get_detailed_desc() + '\n'

    def __init__(self):
        self.set_detailed_desc("Here must be description, but here isn't")
        self.parameters = list()
        self.keywords = list()

    def add_parameter(self, attribute):
        self.parameters.append(attribute)
