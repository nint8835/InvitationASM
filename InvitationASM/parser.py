from typing import List
import ast
import io
import logging

from .exceptions import ParserException
from .operations import TOKENS

logger = logging.getLogger("Parser")


class Statement(object):

    def __init__(self, operation, arguments: list):
        """
        Initialize a new statement object
        :param operation: The operation occurring in this statement
        :param arguments: The arguments for this operation
        """
        self.operation = operation
        self.arguments = arguments

    def execute(self):
        """
        Execute the statement
        """
        self.operation.execute(self.arguments)


class Parser(object):

    def __init__(self, log_level: int = logging.WARNING):
        self.logger = logging.getLogger("Parser")
        logging.basicConfig(format="{%(asctime)s} (%(name)s) [%(levelname)s]: %(message)s",
                            datefmt="%x, %X",
                            level=log_level)

    def parse_line(self, line: str) -> Statement:
        """
        Parses a line
        :param line: The line to parse
        :return: The parsed line
        """
        self.logger.debug(f"Parsing line \"{line}\"")

        if line.strip() == "":
            return

        segments = line.split(" ")

        operation = segments[0]
        self.logger.debug(f"    Operation: {operation}")

        if operation not in TOKENS:
            raise ParserException(f"Operation {operation} undefined")

        if len(segments) == 1:
            arguments = []
        else:
            argument_list = "".join(segments[1:]).split(",")
            self.logger.debug(f"    Arguments: {argument_list}")
            arguments = []
            for argument in argument_list:
                try:
                    arg = ast.literal_eval(argument)
                    if not isinstance(arg, int):
                        raise ValueError()
                    else:
                        arguments.append(arg)
                except ValueError:
                    raise ParserException(f"Invalid type for argument {argument}")

        op = TOKENS[operation]

        statement = Statement(op, arguments)

        self.logger.debug(f"    Statement created: {statement}: {operation}, {arguments}")

        return statement

    def parse_file(self, filename: str) -> List[Statement]:
        """
        Parses a file
        :param filename: The file to parse
        :return: The statements in the file
        """
        with open(filename) as f:
            return self.parse_stream(f)

    def parse_stream(self, stream: io.IOBase) -> List[Statement]:
        """
        Parses a stream
        :param stream: The stream to parse
        :return: The statements in the stream
        """
        statements = []
        lines = list(map(lambda x: x.strip(), stream.readlines()))
        for line in lines:
            statement = self.parse_line(line)
            if statement is not None:
                statements.append(statement)

        return statements
