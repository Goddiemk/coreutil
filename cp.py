import argparse, shutil

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='cp gnu utility in python')
parser.add_argument('origin', help='specify the directory of the original location of file want to copy ')
parser.add_argument('dest', help='specify the directory of the destination of file to be copied')
args = parser.parse_args()

try:
    shutil.copy(args.origin, args.dest)
except FileNotFoundError:
    print("Specified directory is not found")
