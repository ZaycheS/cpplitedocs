keywords_list = ['static', 'public', 'private', 'protected', 'const', 'abstract', 'virtual', 'friend', 'local']
st_data_types = ['char', 'int', 'double', 'float', 'void', 'bool']
path = r'D:\test.cpp'
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
useless_keyword_list = ['if', 'while', 'for', 'switch', ]
version=0.1

def parentheses_skip(strings, i, par='{'):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = [par]
    start = True
    i = 0
    while stack and i < len(strings):
        j = 0
        while i<len(strings) and j < len(strings[i]):
            if strings[i][j] in open_list:
                if not start:
                    stack.append(strings[i][j])
                elif strings[i][j] == par:
                    start = False
                else:
                    stack.append(strings[i][j])
            elif strings[i][j] in close_list:
                pos = close_list.index(strings[i][j])
                if ((len(stack) > 0) and
                        (open_list[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return 1
            if strings[i][j] == '\'' or strings[i][j] == '\"':
                string_start = strings[i][j]
                j += 1
                while j < len(strings[i]):
                    if strings[i][j] == string_start:
                        break
                    if strings[i][j] == '\\':
                        j += 1
                    j += 1

            if j+1<len(strings[i]) and strings[i][j] == '/' and strings[i][j + 1] == '/':
                i += 1
                j=0
                continue
            j += 1
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
