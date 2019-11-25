import argparse
from main import *
from generating import *
from util import version

cli_parser = argparse.ArgumentParser(description="Generate documentation for cpp code")
# group = cli_parser.add_mutually_exclusive_group(required=True)
# group.add_argument("-f", "--file", action="store_true", help="parse file at <path>")
# group.add_argument("-d", "--directory", action="store_true", help="parse all files in <path> directory")
# group.add_argument("-a", "--all", action="store_true", help="parse all files and directories in <path> directory")
# cli_parser.add_argument("path", help="path to files")

args = cli_parser.parse_args()
generate_dirtree(r"D:\ok")
generate_main_page(os.path.basename(args.path),version,0,0,0,0)
# if args.file:
#     file_parsing(args.path)
# elif args.directory:
#     dir_parsing(args.path)
# elif args.all:
#     all_parsing(args.path)
