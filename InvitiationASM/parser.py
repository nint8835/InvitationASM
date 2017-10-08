from .exceptions import ParserException


class Statement(object):

    def __init__(self, operation, arguments):
        self.operation = operation
        self.arguments = arguments


class Parser(object):

    def parse_line(self, line: str) -> Statement:
        segments = line.split(" ")
        if len(segments) < 2:
            raise ParserException(f"Statement must consist of 2 parts, not {len(segments)}")
        operation = segments[0]
        arguments = "".join(segments[1:]).split(",")
