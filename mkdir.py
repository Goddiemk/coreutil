import argparse,pathlib

parser=argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='dir gnu utility in python')
parser.add_argument('path',help='specify the directory want to be created')
parser.add_argument('-p','--parents',help='make parent directories as needed',action='store_true')
args=parser.parse_args()

try:
    if args.path and args.parents:
        pathlib.Path(args.path).mkdir(parents=True)
    if args.path:
        try:
            pathlib.Path(args.path).mkdir()
        except:
            FileNotFoundError
            print("File not found")
except:
    FileExistsError
    print("File exists")



