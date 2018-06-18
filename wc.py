import argparse, fileinput, os

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='wc gnu utility in python')
parser.add_argument('path', help='specify a file directory', nargs='+')
parser.add_argument('-m', '--chars', action='store_true', help='print the character counts')
parser.add_argument('-l', '--lines', action='store_true', help='print the new line counts')
parser.add_argument('-w', '--words', action='store_true', help='print the word counts')
parser.add_argument('-c', '--bytes', action='store_true', help='print the byte counts')
args = parser.parse_args()

try:
    charcount = wordcount = 0
    with fileinput.input(files=(args.path)) as f:
        for line in f:
            linecount = fileinput.lineno()
            wordcount += len(line.split(None))
            charcount += len(line)
    if args.chars:
        print(charcount)
    elif args.lines:
        print(linecount)
    elif args.words:
        print(wordcount)
    elif args.bytes:
        print(charcount)
    else:
        print("%d %d %d %s" % (linecount, wordcount, charcount, args.path))

except FileNotFoundError:
    print("File %s not found" % args.path)
    raise SystemExit
