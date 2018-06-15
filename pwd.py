import os,sys,argparse

def main():
    parser=argparse.ArgumentParser(description="",add_help=False)
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                        help='Print the full filename of the current working directory.')
    args=parser.parse_args()
    print (os.getcwd())
    sys.exit(0)


if __name__ == "__main__":
    main()
