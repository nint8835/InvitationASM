import logging
import argparse

from InvitationASM.interpreter import load_file, run


parser = argparse.ArgumentParser(description="Execute an InvitationASM program.")
parser.add_argument("-e", action="store_true", dest="extensions_enabled", help="enable InvitationASM extensions", default=False)
parser.add_argument("-v", action="store_true", dest="verbose_enabled", help="enable debug output", default=False)
parser.add_argument("filename", help="path to the file to run")
args = parser.parse_args()

if args.extensions_enabled:
    from extensions import *

if args.verbose_enabled:
    loglevel = logging.DEBUG
else:
    loglevel = logging.WARNING

load_file(args.filename, loglevel)
run()