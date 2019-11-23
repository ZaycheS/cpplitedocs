from util import *
from description import Description
from ClassDesc import ClassDesc
from class_parser import class_parser
from method_pars import method_parser
from namespace import NamespaceDesc
from namespace_parser import namespace_parser
from typename import TypeName
from structor import StructorDesc
from structor_parser import structor_parser
from enumdesc import EnumDesc
from enum_parser import enum_parser
import os


def file_iteration(rootdir=r'D:\Veps'):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(os.path.join(subdir, file))


def structor_check(string, class_name=None):
    def_string = string.split()
    j = 0
    for j in range(len(def_string)):
        if def_string[j] in keywords_list:
            continue
        else:
            if def_string[j].find('(') != -1:
                # and (                   def_string[j].split('(', 1)[0] == class_name or def_string[j].split('(', 1)[0] == '~' + class_name):
                return True
            else:
                return False
    return False


def method_signature_check(string):
    defString = string.split()
    for j in range(len(defString)):
        if defString[j] in keywords_list:
            continue
        else:
            j += 1
            if j < len(defString) and defString[j].find('(') != -1 and defString[j].split('(', 1)[
                0].strip() != '':
                return True
            else:
                return False


def attr_signature_check(string):
    defString = string.split()
    for j in range(len(defString)):
        if defString[j] in keywords_list:
            continue
        else:
            pr_type = defString[j].replace('*', '')
            pr_name = defString[j].replace(';', '')
            if (pr_type in st_data_types or pr_type.isidentifier()) and pr_name.isidentifier():
                return True
            else:
                return False


def parser(strings, descs_list, parent=None):
    detailed_desc = ''
    brief_desc = ''
    __detailed_desc = False
    i = 0
    while i < len(strings):
        if first_word_check(strings[i], 'enum'):
            temp_enum = EnumDesc()
            i += enum_parser(strings[i:], temp_enum)
            descs_list.append(temp_enum)
        elif first_word_check(strings[i], '//!'):
            brief_desc = strings[i].strip()[3:]
            i += 1
        elif first_word_check(strings[i], ['/**', '/*!']):
            __detailed_desc = True
            detailed_desc = ' '.join(strings[i].split()[1::])
            i += 1
        elif __detailed_desc:
            if strings[i].endswith('*/\n'):
                __detailed_desc = False
            elif first_word_check(strings[i], '*'):
                detailed_desc += ' '.join(strings[i].split()[1::])
            else:
                detailed_desc += strings[i]
            i += 1
        elif first_word_check(strings[i], '#include'):
            include = strings[i].replace('\n', '')
            includes.append(include[9:])
            i += 1
        elif first_word_check(strings[i], '#define'):
            include = strings[i].replace('\n', '')
            includes.append(include)
            i += 1
        elif first_word_check(strings[i], ['class', 'struct']):
            temp_class_desc = ClassDesc()
            body_length = class_parser(strings[i:], temp_class_desc)
            parser(strings[i + 1:i + body_length], temp_class_desc.descs_list, temp_class_desc)
            i += body_length
            descs_list.append(temp_class_desc)
        elif first_word_check(strings[i], 'namespace'):
            temp_namespace_desc = NamespaceDesc()
            body_length = namespace_parser(strings[i:], temp_namespace_desc)
            parser(strings[i + 1:i + body_length], temp_namespace_desc.descs_list)
            i += body_length
            descs_list.append(temp_namespace_desc)
        elif method_signature_check(strings[i]):
            method_desc = MethodDesc()
            if detailed_desc != '':
                method_desc.set_detailed_desc(detailed_desc)
                detailed_desc = ''
            if brief_desc != '':
                method_desc.set_brief_desc(brief_desc)
                brief_desc = ''
            i += method_parser(strings[i:], method_desc)
            descs_list.append(method_desc)
        elif attr_signature_check(strings[i]):
            defString = strings[i].split()
            temp_attr = TypeName('', '')
            for l in range(len(defString)):
                if defString[l] in keywords_list:
                    temp_attr.add_keyword(defString[l])
                else:
                    temp_attr.set_type(defString[l])
                    temp_attr.set_name(defString[l + 1].replace(';', ''))
                    break
            if brief_desc != '':
                temp_attr.set_brief_desc(brief_desc)
                brief_desc = ''
            if detailed_desc != '':
                temp_attr.set_detailed_desc(detailed_desc)
                detailed_desc = ''
            descs_list.append(temp_attr)
            i += 1
        elif structor_check(strings[i]):
            structor_desc = StructorDesc()
            if detailed_desc != '':
                structor_desc.set_detailed_desc(detailed_desc)
                detailed_desc = ''
            if brief_desc != '':
                structor_desc.set_brief_desc(brief_desc)
                brief_desc = ''
            i += structor_parser(strings[i:], structor_desc)
            descs_list.append(structor_desc)
        else:
            i += 1


class MethodDesc(Description):
    name = ''
    type = ''
    attributes = list()

    def __str__(self):
        return 'Description of ' + self.name + ' type:' + self.type + ' attributes:' + ' '.join(
            map(str, self.attributes)) + '\nKeywords:' + ' '.join(
            map(str,
                self.keywords)) + '\nBrief description:' + self.get_brief_desc() + '\nDetailed desription:\n' + self.get_detailed_desc()

    def __init__(self):
        self.comment = "Here must be description, but here isn't"
        self.attributes = list()
        self.keywords = list()

    def add_parameter(self, attribute):
        self.attributes.append(attribute)


def includes_check(include_list):
    comment = False
    includes = []
    for i in include_list:
        if i.startswith('\"'):
            file2 = open("d:\\" + i.replace('\"', ''))
            strings2 = file2.readlines()
            for i in range(len(strings2)):
                if comment:
                    if strings2[i].endswith('*/\n'):
                        comment = False
                    continue
                if strings2[i].startswith('/*'):
                    comment = True
                    continue
                if strings2[i].startswith('#include'):
                    include = strings2[i].replace('\n', '')
                    includes.append(include[9:])
                    continue
                if strings2[i].startswith('#define'):
                    include = strings2[i].replace('\n', '')
                    includes.append(include)
                    continue
            print(includes)


def first_word_check(string, check):
    if isinstance(check, str):
        if len(string.split(maxsplit=1)) > 0 and string.split(maxsplit=1)[0] == check:
            return True
        else:
            return False
    elif len(string.split(maxsplit=1)) > 0 and string.split(maxsplit=1)[0] in check:
        return True
    else:
        return False


file = open(path, 'r')
strings = file.readlines()
includes = list()

file_desc_list = list()
parser(strings, file_desc_list)
# for i in range(len(includes)):
#     print(includes[i])
for i in range(len(file_desc_list)):
    print(file_desc_list[i])

# includesCheck(includes)
