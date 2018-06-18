import argparse, fileinput

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='tac gnu utility in python')
parser.add_argument('path', help='specify a file with directory to display its text in reverse')
args = parser.parse_args()

str1=''.join(args.path)
with open(str1,'r') as file:
    lines=file.readlines()
for relines in reversed(lines):
    print(relines.rstrip())