Для використання необхідно,знаходячись у папці з файлами cpplitedocs, запустити CLI.py.
За допомогою команди dirpath>CLI.py -help(dirpath>python CLI.py -help) можна отримати таку довідку:
usage: CLI.py [-h] (-f | -d | -a) path name version

Generate documentation for cpp code

positional arguments:
  path             Path to files
  name             Name of project
  version          Version of project

optional arguments:
  -h, --help       show this help message and exit
  -f, --file       parse file at <path>
  -d, --directory  parse all files in <path> directory
  -a, --all        parse all files and directories in <path> directory
   
   Запис головної сторінки,індексу та дерева відбувається у папку "1\"
   Запис документації файлів у папку "1\items\"
