from util import *
from attribute import Attribute


def only_one_str_handler(string, method_desc):
    init_str = string.split()
    i = 0
    while init_str[i] in keywords_list:
        method_desc.add_keyword(init_str[i])
        i += 1
    method_desc.type = init_str[i]
    method_desc.name = init_str[i + 1].split('(', 1)[0]
    attributes = (init_str[i + 1].split('(', 1)[1] + ' ' + ' '.join(init_str[i + 2:])).split(',')
    m = 0
    while m < len(attributes) - 1:
        attribute = Attribute()
        attr_comp = attributes[m].split()
        j = 0
        while attr_comp[j] in keywords_list:
            attribute.add_keyword(attr_comp[j])
            j += 1
        attribute.set_type(attr_comp[j])
        attribute.set_name(attr_comp[j + 1])
        method_desc.add_attribute(attribute)
        m += 1
    if attributes[len(attributes) - 1] != '':
        attribute = Attribute()
        attr_comp = attributes[len(attributes) - 1].split()
        j = 0
        while attr_comp[j] in keywords_list:
            attribute.add_keyword(attr_comp[j])
            j += 1
        if not attr_comp[j].startswith('void)'):
            attribute.set_type(attr_comp[j])
            if attr_comp[j + 1].find(')') != -1:
                attribute.set_name(attr_comp[j + 1].split(')', 1)[0])
                method_desc.add_attribute(attribute)
                return True
        else:
            return True
    return False


def method_parser(strings, method_desc):
    if only_one_str_handler(strings[0], method_desc):
        return 1
    else:
        i = 1
        while i < len(strings):
            attributes = (' '.join(strings[i].split())).split(',')
            for k in range(len(attributes) - 1):
                attribute = Attribute()
                attr_comp = attributes[k].split()
                j = 0
                while attr_comp[j] in keywords_list:
                    attribute.add_keyword(attr_comp[j])
                    j += 1
                attribute.set_type(attr_comp[j])
                attribute.set_name(attr_comp[j + 1])
                method_desc.add_attribute(attribute)
            if attributes[len(attributes) - 1] != '':
                attribute = Attribute()
                attr_comp = attributes[len(attributes) - 1].split()
                j = 0
                while attr_comp[j] in keywords_list:
                    attribute.add_keyword(attr_comp[j])
                    j += 1
                attribute.set_type(attr_comp[j])
                if attr_comp[j + 1].find(')') != -1:
                    attribute.set_name(attr_comp[j + 1].split(')', 1)[0])
                    method_desc.add_attribute(attribute)
                    return i
            i += 1
        return -1
