from util import *
from typename import TypeName


def class_def_handler(class_def, class_desc):
    class_def_words = class_def.split()
    if len(class_def_words) > 1:
        class_desc.set_name(class_def_words[1].replace('{', '').replace(';', ''))
    else:
        class_desc.set_name("DEFAULT")

    if len(class_def_words) > 2 and class_def.find(':') != -1:
        parent_defs = class_def.split(':', 1)[1].split()
        for parent_def_str in ' '.join(parent_defs).split(','):
            temp_parent = TypeName()
            parent_def = parent_def_str.split()
            j = 0
            for j in range(len(parent_def)):
                if parent_def[j] in keywords_list:
                    temp_parent.add_keyword(parent_def[j])
                else:
                    break

            temp_parent.set_name(parent_def[j].replace('{', '').replace(';', ''))
            class_desc.add_parent(temp_parent)


def class_parser(strings, class_desc):
    i = 0
    stop = False
    while not stop and i < len(strings):
        for j in strings[i]:
            if j == ';' or j == '{':
                stop = True
        i += 1
    class_str = ''
    for j in range(0, i):
        class_str += strings[j].strip()
    class_def_handler(class_str, class_desc)
    if not class_str.endswith(';'):
        k = parentheses_skip(strings, i, '{')
    else:
        k = 0
    return k, i
