import argparse, fileinput

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='wc gnu utility in python')
parser.add_argument('path', help='specify a file with directory to display its text', nargs="+")
args = parser.parse_args()

try:
    charcount = wordcount = 0
    for line in fileinput.input():
        linecount = fileinput.lineno()
        wordcount += len(line.split(None))
        charcount += len(line)
    print("%d %d %d %s" % (linecount, wordcount, charcount, args.path))
except FileNotFoundError:
    print("File %s not found" % args.path)
    raise SystemExit
