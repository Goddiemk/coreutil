ver = (2, 0)

import os
import sys

def usage(cmd):
    print "Usage: %s [OPTION]" % (cmd,)
    print "Print the full filename of the current working directory.\n"
    print "      --help     display this help and exit"
    print "      --version  output version information and exit\n"
    print "NOTE: your shell may have its own version of pwd, which usually supercedes"
    print "the version described here.  Please refer to your shell's documentation"
    print "for details about the options it supports."

def main():
    prog = os.path.basename(sys.argv[0])

    if len(sys.argv) == 1:
        print os.getcwd()
        sys.exit(0)

    if sys.argv[1] == "--help":
        usage(prog)
        sys.exit(0)
    elif sys.argv[1] == "--version":
        print "pycoreutils %s version %d.%d" % (prog, ver[0], ver[1],)
        sys.exit(0)
    else:
        sys.stderr.write("%s: extra operand `%s'" % (prog, sys.argv[1],))
        sys.stderr.write("Try `%s --help' for more information." % (prog,))
        sys.exit(1)

if __name__ == "__main__":
    main()