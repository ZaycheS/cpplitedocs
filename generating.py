import datetime
import os
from util import *
from ClassDesc import ClassDesc
from namespace import NamespaceDesc
from enumdesc import EnumDesc


def iterate_through(descs_list, parent_name=None, big_types=(ClassDesc, NamespaceDesc, EnumDesc)):
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
            result = iterate_through(i.descs_list, parent_name)
            cards += result[0]
            names += result[1]
    return cards, names


def generate_main_page(name, ver, desc):
    print("Generating main page")
    f = open("mainpage.html", 'r')
    a = f.read()
    a = a.replace("%README%", desc)
    a = a.replace("%DOCNAME%", name)
    a = a.replace("%DOCVER%", str(ver))
    a = a.replace("%DOCDATE%", str(datetime.datetime.today()))
    result = open("1/mainpage.html", "w")
    result.write(a)


def generate_index(list_names, name):
    list_names.sort(reverse=True)
    f = open("index.html", 'r')
    a = f.read()
    a = a.replace("%DOCNAME%", name)
    for i in list_names:
        if len(i[0]) > 0:
            letter = i[0][0]
            finder = ""
            finder += "<h1><span class=\"badge badge-secondary\">" + letter.upper() + "</span></h1><br>"
            index = a.find(finder)
            if index >= 0:
                print(i)
                card = '<div class="row"><div class="col-sm-3 col-md-6 col-lg-4">' + "<a href=\"items/" + i[
                    1] + ".html#" + i[0] + "\">" + i[
                           0] + "</a>" + ' </div><div class="col-sm-9 col-md-6 col-lg-8"' + '>' + \
                       i[
                           1] + '</div></div>'
                a = insert_char(a, index + len(finder), card)
    result = open("1/index.html", "w+")
    result.write(a)


def generate_dirtree(rootdir, type, name):
    print("Generating dirtree")

    start = "<div class=\"list-group list-group-root well\">"
    f = open("dirtree.html", 'r')
    a = f.read()
    a = a.replace('%DOCNAME%', name)
    insertion = ""
    main_ws = rootdir.count("\\")
    if type == 0:
        tree = os.walk(rootdir)
        count = 0
        for i in tree:
            emptydir = True
            ws = i[0].count("\\") - main_ws
            if len(i[2]) > 0:
                for k in i[2]:
                    if k.endswith(".cpp") or k.endswith('.h') or k.endswith('.hxx'):
                        emptydir = False
                if not emptydir:
                    insertion += "<a class =\"list-group-item list-group-item-secondary\" >" + "<pre>" + ws * "  " + (
                        os.path.relpath(i[0], start=rootdir) if i[0] != rootdir else i[0]) + "</pre>" + "</a>"
                    for j in i[2]:
                        if j.endswith(".cpp") or j.endswith('.h') or j.endswith('hxx'):
                            count += 1
                            insertion += (
                                    "<a  href = \"items/" + j + ".html\" class =\"list-group-item list-group-item-action list-group-item-primary\">" + "<pre>" + (
                                    ws + 1) * "  " + j + "</pre>" + "</a>")
                else:
                    insertion += "<a class =\"list-group-item list-group-item-secondary\" >" + "<pre>" + ws * "  " + (
                        os.path.relpath(i[0], start=rootdir) if i[0] != rootdir else i[0]) + "</pre>" + "</a>"

    elif type == 1:
        insertion += "<a class =\"list-group-item\" >" + rootdir + "</a>"
        ws = rootdir[0].count("/")
        for filename in os.listdir(rootdir):
            if filename.endswith(".cpp") or filename.endswith(".h") or filename.endswith(".hxx"):
                insertion += (
                        "<a  href = \"items/" + filename + ".html\" class =\"list-group-item list-group-item-action list-group-item-primary\">" + "<pre>" + (
                        ws + 1) * "  " + filename + "</pre>" + "</a>")
    else:
        insertion += "<a  href = \"items/" + os.path.basename(
            rootdir) + ".html\" class =\"list-group-item list-group-item-action list-group-item-primary\">" + "<pre>" + os.path.basename(
            rootdir) + "</pre>" + "</a>"
    index = a.find(start)
    # print(index)
    a = insert_char(a, index + len(start), insertion)

    result = open("1/dirtree.html", "w+")
    result.write(a)


def generate_item(file_desc, includes, filename, name):
    f = open("item.html", 'r')
    a = f.read()
    fusingline = " <h3>Included files:</h3>\n"
    fnamesline = "<h3>Members list</h3>\n<ol class=\"list-group\" style=\"left:20px\">"
    cards = "<h3>Detailed descriptions</h3>\n <hr>"
    result = iterate_through(file_desc)

    for k in includes:
        fusingline += k + "\n"
    fnamesline += result[1]
    filename = os.path.basename(filename)
    fnamesline += "</ol>"
    a = a.replace("<h3>Import directives</h3>", fusingline)
    a = a.replace("<h3>Members list</h3>", fnamesline)
    cards += result[0]
    a = a.replace("<h3>Detailed descriptions</h3>", cards)
    a = a.replace("%DOCNAME%", name)
    a = a.replace('\\code', '<code>')
    a = a.replace('\\endcode', '</code>')
    a = a.replace("\\deprecated", "<strong>DEPRECATED</strong>")
    a = a.replace("%ITEMNAME%", filename)
    result = open("1/items/" + filename + ".html", "w+")
    result.write(a)


def insert_char(mystring, position, chartoinsert):
    longi = len(mystring)
    mystring = mystring[:position] + chartoinsert + mystring[position:]
    return mystring
