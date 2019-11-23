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
    if structor_desc.name.startswith('~'):
        structor_desc.type=False
    else:
        structor_desc.type=True
    ending = string.split('(')[1].split(')')
    params = ending[0].split(',')
    after_keywords = ending[1].split()
    for ends in after_keywords:
        if ends in keywords_list:
            structor_desc.add_keyword(ends)

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
        structor_desc.add_parameter(param)


def structor_parser(strings, method_desc):
    i = parentheses_skip(strings, 0, '(')
    method = ''
    for j in range(0, i):
        method += strings[j].strip()
    structor_str_handler(method, method_desc)
    k=parentheses_skip(strings,i)
    return k
