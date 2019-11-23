from util import *
from typename import TypeName

def method_str_handler(string, method_desc):
    init_str = string.strip().split()
    for i in range(len(init_str)):
        if init_str[i] in keywords_list:
            method_desc.add_keyword(init_str[i])
        else:
            break
    else:
        return
    method_desc.type = init_str[i]
    method_desc.name = init_str[i + 1].split('(', 1)[0]
    ending = string.split('(')[1].split(')')
    params = ending[0].split(',')
    after_keywords = ending[1].split()
    for ends in after_keywords:
        if ends in keywords_list:
            method_desc.add_keyword(ends)
    for param in params:
        parameter = TypeName()
        param_comps = param.split()
        for j in range(len(param_comps)):
            if param_comps[j] in keywords_list:
                parameter.add_keyword(param_comps[j])
            else:
                break
        else:
            continue
        if param_comps[j] == 'void':
            continue
        parameter.set_type(param_comps[j].strip())
        parameter.set_name(param_comps[j + 1].strip())
        method_desc.add_parameter(parameter)


def method_parser(strings, method_desc):
    i = parentheses_skip(strings, 0, '(')
    method = ''
    for j in range(0, i):
        method += strings[j].strip()
    method_str_handler(method, method_desc)
    k=parentheses_skip(strings,i)
    return k
