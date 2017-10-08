from typing import List
import ast
import io

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

        argument_list = "".join(segments[1:]).split(",")
        arguments = list(map(ast.literal_eval, argument_list))
        for argument in arguments:
            if not isinstance(argument, int):
                raise ParserException(f"Statement arguments must be int, not {type(argument)}")

        op = TOKENS[operation]

        return Statement(op, arguments)

    def parse_file(self, filename: str) -> List[Statement]:
        with open(filename) as f:
            return self.parse_stream(f)

    def parse_stream(self, stream: io.IOBase) -> List[Statement]:
        statements = []
        lines = list(map(lambda x: x.strip(), stream.readlines()))
        for line in lines:
            statements.append(self.parse_line(line))

        return statements
