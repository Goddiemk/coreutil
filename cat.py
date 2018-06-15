import argparse, fileinput

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='cat gnu utility in python')
parser.add_argument('path', help='specify a file with directory to display its text', nargs="+")
args = parser.parse_args()

if args.path:
    for line in fileinput.input():
        print(line, end="")
