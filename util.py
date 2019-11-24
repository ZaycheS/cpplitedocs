keywords_list = ['static', 'public', 'private', 'protected', 'const', 'abstract', 'virtual', 'friend','local']
st_data_types = ['char', 'int', 'double', 'float', 'void', 'bool']
path = r'D:\test.cpp'
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
useless_keyword_list = ['if', 'while', 'for', 'switch', ]


def parentheses_skip(strings, i, par='{'):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = [par]
    start = True
    while stack and i < len(strings):
        for j in strings[i]:
            if j in open_list:
                if not start:
                    stack.append(j)
                elif j == par:
                    start = False
                else:
                    stack.append(j)
            elif j in close_list:
                pos = close_list.index(j)
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return 1
        if stack:
            i += 1
    return i + 1


def string_parentheses_skip(string, par='{'):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = [par]
    i = 0
    j = 0
    par_list = list()
    while stack and i < len(string):
        if string[i] in open_list:
            stack.append(string[i])
        elif string[i] in close_list:
            pos = close_list.index(string[i])
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return 1
        elif string[i] == ',' and len(stack) == 1:
            par_list.append(string[j:i])
            j = i + 1
        i += 1
    par_list.append(string[j:i - 1])
    return par_list, i
