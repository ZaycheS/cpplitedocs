from util import *
from typename import TypeName


def enum_def_handler(enum_def, enum_desc):
    enum_def_words = enum_def.split()
    if len(enum_def_words) > 1 and enum_def_words[1].replace('{','')!="":
        enum_desc.set_name(enum_def_words[1].replace('{',''))
    else:
        enum_desc.set_name("DEFAULT")
    temp_parent = TypeName()

    if len(enum_def_words) > 2 and enum_def_words[2] == ':':
        parent_def = enum_def_words[3:]
        j = 0
        for j in range(len(parent_def)):
            if parent_def[j] in keywords_list:
                temp_parent.add_keyword(parent_def[j])
            else:
                break
        temp_parent.set_name(parent_def[j])
        enum_desc.set_parent(temp_parent)


def enum_parser(strings, enum_desc):
    enum_def_handler(strings[0], enum_desc)
    i = parentheses_skip(strings, 0, '{')
    return i
