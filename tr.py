import argparse, re

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='tr gnu utility in python')
parser.add_argument('set1', help='specify the set1')
parser.add_argument('set2', help='specfiy the set2')
parser.add_argument('source', help='specify the string pattern wanted')
parser.add_argument('-c', '--complement', help='use the complement of set1', action='store_true')
parser.add_argument('-d', '--delete', help='delete characters in set1', action='store_true')
parser.add_argument('-s', '--squeeze', help='replace each sequence of a repeated character that is listed in'
                                            'the last specified SET, with a single occurrence of that character',
                    action='store_true')
args=parser.parse_args()
if args.squeeze:
    for char in args.set1:
        pattern = '%s{2,}' % re.escape(char)
        args.source = re.sub(pattern, char, args.source)
    print(args.source)
elif args.delete:
    for char in args.set1:
        args.source = re.sub(char, '', args.source)
    print(args.source)
elif args.complement:
    for char in args.set1:
        pattern = '[^%s]' % args.set1
        args.source = re.sub(pattern, args.set2, args.source)
    print(args.source)
else:
    args = parser.parse_args()
    source = '%s' % args.source
    final = source.translate(str.maketrans(args.set1, args.set2))
    print(final)
