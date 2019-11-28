import argparse
from main import *
from generating import *
from util import version

cli_parser = argparse.ArgumentParser(description="Generate documentation for cpp code")
group = cli_parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", action="store_true", help="parse file at <path>")
group.add_argument("-d", "--directory", action="store_true", help="parse all files in <path> directory")
group.add_argument("-a", "--all", action="store_true", help="parse all files and directories in <path> directory")
cli_parser.add_argument("path", help="Path to files")
cli_parser.add_argument("name", help="Name of project")
cli_parser.add_argument("version", help="Version of project")
args = cli_parser.parse_args()
if args.file:
    file_parsing(args.path,args.name,args.version)
elif args.directory:
    dir_parsing(args.path,args.name,args.version)
elif args.all:
    all_parsing(args.path,args.name,args.version)
else:
    pass
