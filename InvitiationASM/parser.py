from typing import List

from .exceptions import ParserException
from .operations import TOKENS


class Statement(object):

    def __init__(self, operation, arguments: list):
        self.operation = operation
        self.arguments = arguments

    def execute(self):
        self.operation.execute(self.arguments)


class Parser(object):

    def parse_line(self, line: str) -> Statement:
        segments = line.split(" ")
        if len(segments) < 2:
            raise ParserException(f"Statement must consist of 2 parts, not {len(segments)}")

        operation = segments[0]
        if operation not in TOKENS:
            raise ParserException(f"Operation {operation} undefined")

        arguments = "".join(segments[1:]).split(",")

        op = TOKENS[operation]

        return Statement(op, arguments)

    def parse_file(self, filename: str) -> List[Statement]:
        statements = []
        with open(filename) as f:
            for line in f:
                statements.append(self.parse_line(line))

        return statements
