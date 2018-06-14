import os,sys,argparse

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--helpp", help="Your help" ,action="store_true")
    args=parser.parse_args()
    if args.helpp:
        print ("Print the full filename of the current working directory.\n")
        print ("      --help     display this help and exit")
        print ("      --version  output version information and exit\n")
        print ("NOTE: your shell may have its own version of pwd, which usually supercedes")
        print ("the version described here.  Please refer to your shell's documentation")
        print ("for details about the options it supports.")
        sys.exit(0)

    else:
        print (os.getcwd())
        sys.exit(0)


if __name__ == "__main__":
    main()
