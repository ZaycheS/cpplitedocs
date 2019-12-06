from util import *
from typename import TypeName


def structor_str_handler(string, structor_desc):
    init_str = string.strip().split()
    for i in range(len(init_str)):
        if init_str[i] in keywords_list:
            structor_desc.add_keyword(init_str[i])
        else:
            break
    else:
        return
    structor_desc.name = init_str[i].split('(', 1)[0]
    if structor_desc.name.find('~')!=-1:
        structor_desc.type = False
    else:
        structor_desc.type = True
    ending = string.split('(', 1)[1]
    params = string_parentheses_skip(ending, '(')[0]

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
            if j+2<len(param_comps) and param_comps[j+1]== '*':
                parameter.set_name(param_comps[j+1].strip()+param_comps[j+2].strip())
            else:
                parameter.set_name(param_comps[j + 1].strip())
            structor_desc.add_parameter(parameter)


def structor_parser(strings, structor_desc):
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
    structor_str_handler(method, structor_desc)
    if method.strip().endswith(';'):
        return max(i,1)
    k = parentheses_skip(strings, 0)

    return max(k,1)
