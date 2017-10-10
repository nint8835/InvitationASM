import sys
import logging

from InvitationASM.interpreter import load_file, run

args = sys.argv

if len(args) < 2:
    print("Usage: python ExecuteIASM.py <file.iasm>")

filename = args[1]
if "-v" in args:
    load_file(filename, logging.DEBUG)
else:
    load_file(filename)
run()
