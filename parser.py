from method_pars import *
from util import *


def parentheses_skip(strings, i, par='{'):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = [par]
    start = True
    while stack and i <= len(strings):
        for j in strings[i]:
            if j in open_list:
                if not start:
                    stack.append(j)
                else:
                    start = False
            elif j in close_list:
                pos = close_list.index(j)
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return -1
        if stack:
            i += 1
    return i + 1


class MethodDesc:
    comment = ''
    name = ''
    type = ''
    attributes = list()
    keywords = list()

    # def __init__(self, d, c):
    #     self.attributes = list()
    #     self.comment = ' '.join(c.split())
    #     def_string = d[0].split()
    #     i = 0
    #     while def_string[i] in keywords_list:
    #         i += 1
    #     self.type = def_string[i]
    #     self.name = def_string[i + 1][:def_string[i + 1].find('('):]
    #     definition = def_string[i + 1][def_string[i + 1].find('(') + 1::]
    #     for k in range(i + 2, len(def_string)):
    #         definition += ' ' + ' '.join(def_string[k].split())
    #     for j in range(1, len(d)):
    #         definition += ' ' + ' '.join(d[j].split())
    #     attributes = definition.split(',')
    #
    #     for i in range(len(attributes) - 1):
    #         attribute = attributes[i].split()
    #         self.attributes.append(Attribute(attribute[0], attribute[1]))
    #     attribute = attributes[len(attributes) - 1].split()
    #     attribute[1] = attribute[1][:attribute[1].find(')'):]
    #     self.attributes.append(Attribute(attribute[0], attribute[1]))
    def __str__(self):
        return 'Description of ' + self.name + ' type:' + self.type + ' attributes:' + ' '.join(
            map(str, self.attributes)) + '\nComment:' + self.comment

    def __init__(self):
        self.attributes = list()
        self.keywords = list()

    def add_attribute(self, attribute):
        self.attributes.append(attribute)

    def add_keyword(self, keyword):
        self.keywords.append(keyword)


def includes_check(include_list):
    comment = False
    includes = []
    for i in include_list:
        if i.startswith('\"'):
            file2 = open("d:\\" + i.replace('\"', ''))
            strings2 = file2.readlines()
            for i in range(len(strings2)):
                if comment:
                    if strings2[i].endswith('*/\n'):
                        comment = False
                    continue
                if strings2[i].startswith('/*'):
                    comment = True
                    continue
                if strings2[i].startswith('#include'):
                    include = strings2[i].replace('\n', '')
                    includes.append(include[9:])
                    continue
                if strings2[i].startswith('#define'):
                    include = strings2[i].replace('\n', '')
                    includes.append(include)
                    continue
            print(includes)


def first_word_check(string, check):
    if isinstance(check, str):
        if len(string.split(maxsplit=1)) > 0 and string.split(maxsplit=1)[0] == check:
            return True
        else:
            return False
    elif len(string.split(maxsplit=1)) > 0 and string.split(maxsplit=1)[0] in check:
        return True
    else:
        return False


file = open(path, 'r')
strings = file.readlines()
comment = False
includes = list()
descList = []
temp_comment = ''


class EnumDesc:
    name = ' '

    def __init__(self, strings):
        self.name = strings[0].split()[1]
        print(self.name)

    def __str__(self):
        return "Enumeration name:" + self.name


class ClassDesc:
    name = ' '
    methods_list = []

    def __init__(self, strings):
        self.name = strings[0].split()[1]

    def __str__(self):
        return "Class name:" + self.name


for i in range(len(strings)):
    if first_word_check(strings[i], 'enum'):
        k = parentheses_skip(strings, i)
        EnumDesc(strings[i:k:])
        i = k
        continue
    if first_word_check(strings[i], ['/**', '/*!']):
        comment = True
        temp_comment = ' '.join(strings[i].split()[1::])
        continue
    if comment:
        if strings[i].endswith('*/\n'):
            comment = False
        elif first_word_check(strings[i], '*'):
            temp_comment += ' '.join(strings[i].split()[1::])
        else:
            temp_comment += strings[i]
        continue

    if first_word_check(strings[i], '#include'):
        include = strings[i].replace('\n', '')
        includes.append(include[9:])
        continue
    if first_word_check(strings[i], '#define'):
        include = strings[i].replace('\n', '')
        includes.append(include)
        continue
    if first_word_check(strings[i], 'class'):
        k = parentheses_skip(strings, i)
        ClassDesc(strings[i:k:])
        i = k
        continue

    if first_word_check(strings[i], keywords_list + st_data_types):
        defString = strings[i].split()
        for j in range(len(defString)):
            if defString[j] in keywords_list:
                continue
            else:
                j += 1
                if j<len(defString) and defString[j].find('(') != -1: #check for name before '('
                    method_desc = MethodDesc()
                    i += method_parser(strings[i:], method_desc)
                    descList.append(method_desc)
                break
    # print(strings[i].split(' ',1)[0])
for i in range(len(includes)):
    print(includes[i])
for i in range(len(descList)):
    print(descList[i])

# includesCheck(includes)
