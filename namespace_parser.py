from util import *


def namespace_def_handler(namespace_def, namespace_desc):
    namespace_desc.set_name(namespace_def.split()[1])


def namespace_parser(strings, namespace_desc):
    namespace_def_handler(strings[0], namespace_desc)
    i = parentheses_skip(strings, 0, '{')
    return i
