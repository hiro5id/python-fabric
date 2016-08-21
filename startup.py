#!/usr/bin/env python
import sys
import argparse
from subprocess import call
from subprocess import Popen, PIPE, STDOUT


# sub-command functions
def bash(args):
    call("/bin/bash")

def run_ipython(args):
    call(["/usr/local/bin/ipython"] + sys.argv[2:])
	
def run_fabric(args):
    if len(sys.argv) <= 2:
        call(["/usr/local/bin/fab"] + ["--help"])
    else:
        call(["/usr/local/bin/fab"] + sys.argv[2:])

def run_example(args):
    arguments =["python","/root/dropbox.py"] + sys.argv[2:]
    if len(sys.argv) <= 2:
        arguments = arguments + ["help"]
    output = Popen(arguments, stdout=PIPE, stderr=STDOUT).communicate("n\n")[0]
    print output
	
# create the top-level parser
parser = argparse.ArgumentParser(prog='sebestyen/python-fabric')
#parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help')

# Add a command
parser_bash = subparsers.add_parser('bash', help='run bash')
parser_bash.set_defaults(func=bash)

# Add a command
parser_fab = subparsers.add_parser('fab', help='run the fabric automation utility')
parser_fab.set_defaults(func=run_fabric)
## this 'rest' is special it allows me to pass through remainder arguments without it being caught in this arguments parser
parser_fab.add_argument('rest', nargs=argparse.REMAINDER)

# Add a command
parser_ipython = subparsers.add_parser('ipython', help='run ipython interactive shell')
parser_ipython.set_defaults(func=run_ipython)
#parser_ipython.add_argument('vars', nargs='*')
## this 'rest' is special it allows me to pass through remainder arguments without it being caught in this arguments parser
parser_ipython.add_argument('rest', nargs=argparse.REMAINDER)

# parse the args and call whatever function was selected
args = parser.parse_args()
args.func(args)
