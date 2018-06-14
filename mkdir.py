import argparse,pathlib

parser=argparse.ArgumentParser(add_help=False)

parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='dir gnu utility in python')

parser.add_argument('path',help='specify the directory want to be created')

args=parser.parse_args()

if args.path:
    try:
        pathlib.Path(args.path).mkdir(parents=True)
        print("Directory created")
    except FileExistsError:
        print("Directory exists")

