keywords_list = ['static', 'public', 'private', 'protected', 'const', 'abstract', 'virtual', 'friend']
st_data_types = ['char', 'int', 'double', 'float', 'void', 'bool']
path = r'D:\code.cpp'
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
useless_keyword_list=['if','while','for','switch',]

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
                else:
                    start = False
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
