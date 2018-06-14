import argparse
from contextlib import closing

parser=argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='cat gnu utility in python')
parser.add_argument('path',help='specify a file with directory to display its text')

args=parser.parse_args()

if args.path:
    filename=args.path
    file=open(filename,'r')
    with closing (file) as page:
        for line in page:
            print (line)



