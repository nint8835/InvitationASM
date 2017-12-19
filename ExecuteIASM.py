import logging
import argparse

from InvitationASM.interpreter import load_file, run, preprocess_code


parser = argparse.ArgumentParser(description="Execute an InvitationASM program.")
parser.add_argument("-e", action="store_true", dest="extensions_enabled", help="enable InvitationASM extensions", default=False)
parser.add_argument("-v", action="store_true", dest="verbose_enabled", help="enable debug output", default=False)
parser.add_argument("-p", action="store_true", dest="only_parse", help="only parse the file", default=False)
parser.add_argument("filename", help="path to the file to run")
args = parser.parse_args()

if args.extensions_enabled:
    from extensions import *

if args.verbose_enabled:
    loglevel = logging.DEBUG
else:
    loglevel = logging.WARNING

logging.basicConfig(format="{%(asctime)s} (%(name)s) [%(levelname)s]: %(message)s",
                    datefmt="%x, %X",
                    level=loglevel)

if not args.only_parse:
    load_file(args.filename, loglevel)
    run()
else:
    with open(args.filename) as f:
        processed_file = preprocess_code(list(map(lambda x: x.strip(), f.readlines())))
        print("\n".join(processed_file))
