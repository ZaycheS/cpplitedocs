from util import *
from typename import TypeName


def class_def_handler(class_def, class_desc):
    class_def_words = class_def.split()
    if len(class_def_words) > 1:
        class_desc.set_name(class_def_words[1])
    else:
        class_desc.set_name("DEFAULT")

    if len(class_def_words) > 2 and class_def_words[2] == ':':
        parent_defs = class_def_words[3:]
        for parent_def_str in ' '.join(parent_defs).split(','):
            temp_parent = TypeName()
            parent_def = parent_def_str.split()
            j = 0
            for j in range(len(parent_def)):
                if parent_def[j] in keywords_list:
                    temp_parent.add_keyword(parent_def[j])
                else:
                    break
            temp_parent.set_name(parent_def[j])
            class_desc.add_parent(temp_parent)


def class_parser(strings, class_desc):
    class_def_handler(strings[0], class_desc)
    i = parentheses_skip(strings, 0, '{')
    return i
