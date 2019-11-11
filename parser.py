open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


def parenthesesSkip(strings, i, par='{'):
    stack = [par]
    start = True
    while stack and i<=len(strings):
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
                    return "Unbalanced"
        if stack:
            i+=1
    return i+1

file = open(r'D:\code.cpp', 'r')
strings = file.readlines()
comment = False
includes = list()

print(parenthesesSkip(strings,53,'('))
for i in range(len(strings)):
    if comment:
        if strings[i].endswith('*/\n'):
            comment = False
        continue
    if strings[i].startswith('/*'):
        comment = True
        continue
    if strings[i].startswith('#include'):
        include = strings[i].replace('\n', '')
        includes.append(include)
        continue
    if strings[i].startswith('#define'):
        include = strings[i].replace('\n', '')
        includes.append(include)
        continue
    # print(strings[i])
for i in range(len(includes)):
    print(includes[i])
