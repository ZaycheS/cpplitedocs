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
    method_desc.name = ''
    for k in range(i + 1, len(init_str)):
        if init_str[k].find('(') != -1:
            method_desc.name += ' ' + init_str[k].split('(', 1)[0]
            break
        else:
            method_desc.name += ' ' + init_str[k]
    method_desc.name=method_desc.name.strip()
    ending = string.split('(', 1)[1]
    result = string_parentheses_skip(ending, '(')
    ending = ending[result[1]:]
    params = result[0]
    after_keywords = ending.replace('{', '').replace(';', '').split()
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
        if j + 1 < len(param_comps):
            parameter.set_name(param_comps[j + 1].strip())
            method_desc.add_parameter(parameter)


def method_parser(strings, method_desc):
    # i = parentheses_skip(strings, 0, '(')
    i = 0
    stop = False
    while not stop and i < len(strings):
        for j in strings[i]:
            if j == ';' or j == '{':
                stop = True
        i += 1

    method = ''
    for j in range(0, i):
        method += strings[j].strip()
    method_str_handler(method, method_desc)
    if method.strip().endswith(';'):
        return i
    k = parentheses_skip(strings, 0)
    return k
