from util import *
from typename import TypeName


def class_def_handler(class_def, class_desc):
    class_def_words = class_def.split()
    class_desc.set_name(class_def_words[1])
    temp_parent = TypeName()

    if len(class_def_words) > 2 and class_def_words[2] == ':':
        parent_def = class_def_words[3:]
        j=0
        for j in range(len(parent_def)):
            if parent_def[j] in keywords_list:
                temp_parent.add_keyword(parent_def[j])
            else:
                break
        temp_parent.set_name(parent_def[j])
    class_desc.set_parent(temp_parent)


def class_parser(strings, class_desc):
    class_def_handler(strings[0], class_desc)
    i = parentheses_skip(strings, 0, '{')
    return i
