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
from enum_member import EnumMember
from generating import *
from MethodDesc import MethodDesc
import os
import string


def iterate_through(descs_list, spaces=0, parent_name=None, big_types=(ClassDesc, NamespaceDesc, EnumDesc)):
    cards = ''
    names = ''
    for i in descs_list:
        cards += i.generate_card(parent_name)
        names += i.generate_name()
        if isinstance(i, big_types):
            if isinstance(i, ClassDesc):
                if i.type:
                    parent_name = "Class " + i.name
                else:
                    parent_name = "Structure " + i.name
            elif isinstance(i, NamespaceDesc):
                parent_name = "Namespace " + i.name
            elif isinstance(i, EnumDesc):
                parent_name = "Enumeration " + i.name
            result = iterate_through(i.descs_list, spaces + 1, parent_name)
            cards += result[0]
            names += result[1]
    return cards, names


def structor_check(st_string):
    def_string = st_string.split()
    for j in range(len(def_string)):
        if def_string[j] in keywords_list:
            continue
        else:
            if def_string[j].find('(') != -1:
                return True, st_string
            elif len(def_string) > j + 1 and def_string[j + 1].find('(') != -1 and def_string[j + 1].split('(', 1)[
                0].strip() == '':
                def_string[j + 1] = def_string[j] + def_string[j + 1]
                def_string[j] = ''
                st_string = ' '.join(def_string)
                return True, st_string
            else:
                return False, st_string
    return False, st_string


def method_signature_check(met_string):
    def_string = met_string.split()
    for j in range(len(def_string)):
        if def_string[j] in keywords_list:
            continue
        else:
            j += 1
            for k in range(j, len(def_string)):
                if def_string[k].find('(') != -1:
                    if def_string[k].split('(', 1)[0].strip() != '':
                        return True, met_string
                    elif k > j:
                        def_string[k] = def_string[k - 1] + def_string[k]
                        def_string[k - 1] = ''
                        met_string = ' '.join(def_string)
                        return True, met_string
                    else:
                        return False, met_string
                if def_string[k].find('=')!=-1:
                    return False,met_string
            else:
                return False, met_string
    return False, met_string


def attr_signature_check(attr_string):
    def_string = attr_string.split()
    for j in range(len(def_string)):
        if def_string[j] in keywords_list:
            continue
        else:
            if (j + 1) < len(def_string):
                pr_type = def_string[j].replace('*', '')
                pr_name = def_string[j + 1].replace(';', '').replace('*', '')
                if pr_type.startswith(tuple(string.ascii_letters + '_')) and (
                        pr_name.isidentifier() or pr_name.split('[', 1)[0].isidentifier()):
                    return True
                else:
                    return False
    return False


def parser(strings, descs_list, names_list, parent=None, includes=None, filename="", desc_file=None):
    if desc_file is None:
        desc_file = list()
    if includes is None:
        includes = list()
    defines = list()
    detailed_desc = ''
    brief_desc = ''
    __detailed_desc = False
    i = 0
    while i < len(strings):
        if first_word_check(strings[i], 'typedef'):
            strings[i] = strings[i][strings[i].find('typedef') + 7:]
        if first_word_check(strings[i], '//!'):
            brief_desc = strings[i].strip()[3:]
            i += 1
        elif first_word_check(strings[i], ['/**', '/*!']):
            if not strings[i].endswith('*/\n'):
                __detailed_desc = True
            detailed_desc = ' '.join(strings[i].split()[1::]).replace('*/', '')
            i += 1
        elif __detailed_desc:
            if strings[i].endswith('*/\n'):
                __detailed_desc = False
                if detailed_desc.find("\\file") != -1 or detailed_desc.find("@file") != -1:
                    desc_file.append(detailed_desc)
                    detailed_desc = ''
            elif first_word_check(strings[i], '*'):
                detailed_desc += "<br>" + ' '.join(strings[i].split()[1::])
            else:
                detailed_desc += '<br>' + strings[i]
            i += 1
        elif first_word_check(strings[i], '/*'):
            while i < len(strings) and not strings[i].endswith('*/\n'):
                i += 1
            i += 1
        elif first_word_check(strings[i], '//'):
            i += 1
        elif strings[i].strip().startswith('\'') or strings[i].strip().startswith('\"'):
            i += 1
        elif strings[i].strip().startswith("using"):
            i += 1
        else:
            if strings[i].find('/*') != -1:
                strings[i] = strings[i][:strings[i].find('/*')]
            if strings[i].find('//') != -1:
                strings[i] = strings[i][:strings[i].find('//')]
            if first_word_check(strings[i], '#include'):
                include = strings[i].replace('<', "&lt")
                includes.append("<pre>" + include + "</pre>")
                i += 1
            elif first_word_check(strings[i], '#define'):
                define = strings[i].replace('\n', '')
                defines.append(define)
                i += 1
            elif strings[i].strip().startswith('#'):
                i += 1
                continue
            elif first_word_check(strings[i], 'enum'):
                temp_enum = EnumDesc()
                body_length = enum_parser(strings[i:], temp_enum)
                if detailed_desc != '':
                    temp_enum.set_detailed_desc(detailed_desc)
                    detailed_desc = ''
                if brief_desc != '':
                    temp_enum.set_brief_desc(brief_desc)
                    brief_desc = ''
                parser(strings[i + 1:i + body_length - 1], temp_enum.descs_list, names_list, temp_enum,
                       filename=filename)
                names_list.append(tuple([temp_enum.name, filename]))
                i += body_length
                descs_list.append(temp_enum)
            elif isinstance(parent, EnumDesc):
                if strings[i].strip().split(',')[0] != '' and strings[i].strip().replace('{', '') != '':
                    temp_token = EnumMember()
                    temp_token.set_name(strings[i].strip()[:strings[i].rfind(",")].split()[0].replace(",", ''))
                    names_list.append(tuple([temp_token.name, filename]))
                    if detailed_desc != '':
                        temp_token.set_detailed_desc(detailed_desc)
                        detailed_desc = ''
                    if brief_desc != '':
                        temp_token.set_brief_desc(brief_desc)
                        brief_desc = ''
                    descs_list.append(temp_token)
                i += 1
            elif first_word_check(strings[i], ['class', 'struct']):
                temp_class_desc = ClassDesc()
                if detailed_desc != '':
                    temp_class_desc.set_detailed_desc(detailed_desc)
                    detailed_desc = ''
                if brief_desc != '':
                    temp_class_desc.set_brief_desc(brief_desc)
                    brief_desc = ''
                body_length = class_parser(strings[i:], temp_class_desc)
                temp_class_desc.type = first_word_check(strings[i], 'class')
                if(body_length[0]+body_length[1]>1):
                    parser(strings[i + body_length[1]:i + body_length[0]], temp_class_desc.descs_list, names_list,
                       temp_class_desc, filename=filename)
                names_list.append(tuple([temp_class_desc.name, filename]))
                i += body_length[0] + body_length[1]
                descs_list.append(temp_class_desc)
            elif first_word_check(strings[i], 'namespace'):
                temp_namespace_desc = NamespaceDesc()
                body_length = namespace_parser(strings[i:], temp_namespace_desc)
                parser(strings[i + 1:i + body_length], temp_namespace_desc.descs_list, names_list, filename=filename)
                i += body_length
                names_list.append(tuple([temp_namespace_desc.name, filename]))
                descs_list.append(temp_namespace_desc)
            elif structor_check(strings[i])[0]:
                strings[i] = structor_check(strings[i])[1]
                structor_desc = StructorDesc()
                if detailed_desc != '':
                    structor_desc.set_detailed_desc(detailed_desc)
                    detailed_desc = ''
                if brief_desc != '':
                    structor_desc.set_brief_desc(brief_desc)
                    brief_desc = ''
                i += structor_parser(strings[i:], structor_desc)
                names_list.append(tuple([structor_desc.name, filename]))
                descs_list.append(structor_desc)
            elif method_signature_check(strings[i])[0]:
                strings[i] = method_signature_check(strings[i])[1]
                method_desc = MethodDesc()
                if detailed_desc != '':
                    method_desc.set_detailed_desc(detailed_desc)
                    detailed_desc = ''
                if brief_desc != '':
                    method_desc.set_brief_desc(brief_desc)
                    brief_desc = ''
                i += method_parser(strings[i:], method_desc)
                names_list.append(tuple([method_desc.name, filename]))
                descs_list.append(method_desc)
            elif attr_signature_check(strings[i]):
                def_string = strings[i].split()
                temp_attr = TypeName('', '')
                for l in range(len(def_string)):
                    if def_string[l] in keywords_list:
                        temp_attr.add_keyword(def_string[l])
                    else:
                        temp_attr.set_type(def_string[l])
                        temp_attr.set_name(def_string[l + 1].replace(';', '').split('=', 1)[0])
                        break
                if brief_desc != '':
                    temp_attr.set_brief_desc(brief_desc)
                    brief_desc = ''
                if detailed_desc != '':
                    temp_attr.set_detailed_desc(detailed_desc)
                    detailed_desc = ''
                names_list.append(tuple([temp_attr.name, filename]))
                descs_list.append(temp_attr)
                i += 1
            else:
                i += 1


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


def first_word_check(chk_string, check):
    if isinstance(check, str):
        if len(chk_string.split(maxsplit=1)) > 0 and chk_string.split(maxsplit=1)[0] == check:
            return True
        else:
            return False
    elif len(chk_string.split(maxsplit=1)) > 0 and chk_string.split(maxsplit=1)[0] in check:
        return True
    else:
        return False


def dir_parsing(path, proj_name, proj_ver):
    name_list = list()
    if os.path.isfile(os.path.join(path, "readme.txt")):
        proj_file = open(os.path.join(path, "readme.txt"))
        proj_doc = proj_file.read()
        generate_main_page(proj_name, proj_ver, "<pre>" + proj_doc + "</pre>")
    elif os.path.isfile(os.path.join(path, "README.md")):
        proj_file = open(os.path.join(path, "README.md"))
        proj_doc = proj_file.read()
        generate_main_page(proj_name, proj_ver, "<pre>" + proj_doc + "</pre>")
    else:
        generate_main_page(proj_name, proj_ver, "")
    if os.path.isdir(path):
        for filename in os.listdir(path):
            if filename.endswith(".cpp") or filename.endswith(".h") or filename.endswith(".hxx"):
                file = open(os.path.join(path, filename), 'r')
                strings = file.readlines()
                file_desc_list = list()
                includes = list()
                desc_file=list()
                parser(strings, file_desc_list, name_list, None, includes, filename,desc_file=desc_file)
                generate_item(file_desc_list, includes, filename, proj_name,desc_file=desc_file)
                print(os.path.join(path, os.path.basename(file.name)))
                continue
            else:
                continue
        generate_dirtree(path, 1, proj_name)
        generate_index(name_list, proj_name)
    else:
        print("Not a directory")


def file_parsing(filename, proj_name, proj_ver):
    generate_main_page(proj_name, proj_ver, "")
    if os.path.isfile(filename):
        if filename.endswith(".cpp") or filename.endswith(".h") or filename.endswith(".hxx"):
            file = open(filename, 'r')
            filename = os.path.basename(filename)
            strings = file.readlines()
            name_list = list()
            file_desc_list = list()
            includes = list()
            desc_file=list()
            parser(strings, file_desc_list, name_list, None, includes, filename,desc_file=desc_file)
            generate_item(file_desc_list, includes, filename, proj_name,desc_file)
            generate_index(name_list, proj_name)
            generate_dirtree(filename, 2, proj_name)
    else:
        print("Not a file")


def all_parsing(rootdir, proj_name, proj_ver):
    names_list = list()
    if os.path.isfile(os.path.join(rootdir, "readme.txt")):
        proj_file = open(os.path.join(rootdir, "readme.txt"))
        proj_doc = proj_file.read()
        generate_main_page(proj_name, proj_ver, "<pre>" + proj_doc + "</pre>")
    elif os.path.isfile(os.path.join(rootdir, "README.md")):
        proj_file = open(os.path.join(rootdir, "README.md"))
        proj_doc = proj_file.read()
        generate_main_page(proj_name, proj_ver, "<pre>" + proj_doc + "</pre>")
    else:
        generate_main_page(proj_name, proj_ver, "")
    if os.path.isdir(rootdir):
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                if file.endswith('.h') or file.endswith('.cpp') or file.endswith('.hxx'):
                    file = open(os.path.join(subdir, file), 'r')
                    strings = file.readlines()
                    file_desc_list = list()
                    includes = list()
                    desc_file=list()
                    parser(strings, file_desc_list, names_list, None, includes, os.path.basename(file.name),desc_file=desc_file)
                    generate_item(file_desc_list, includes, os.path.basename(file.name), proj_name,desc_file)
                    print(os.path.join(subdir, os.path.basename(file.name)))
        generate_index(names_list, proj_name)
        generate_dirtree(rootdir, 0, proj_name)
    else:
        print("Not a directory")
