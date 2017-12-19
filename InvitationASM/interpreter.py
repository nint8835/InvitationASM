import logging
from typing import List
import re

from .parser import Parser
from .operations import TOKENS
from .memory import MemoryValue, MEMORY


CODE_LABEL = re.compile(r"^(\w+):$")
DATA_LABEL = re.compile(r"^(\w+): \.data (\d+)$")
ARGUMENTS = re.compile(r"^\w+ (.+)$")


def preprocess_code(data: List[str]) -> List[str]:
    labels = {}
    data_offset = 1000

    new_code = []

    # Generate labels for data sections
    for line in data:
        if DATA_LABEL.match(line):
            results = DATA_LABEL.findall(line)[0]
            labels[results[0]] = data_offset
            new_code.insert(0, f"INIT {data_offset}, {results[1]}")
            data_offset += 1
        else:
            new_code.append(line)

    data = new_code
    new_code = []

    data_length = len(labels)

    # Generate labels for code sections
    for i, line in enumerate(data):
        if CODE_LABEL.match(line):
            labels[CODE_LABEL.findall(line)[0]] = i + 1 - len(labels) + data_length
        else:
            new_code.append(line)

    data = new_code
    new_code = []

    # Replace all label references with memory addresses
    for line in data:
        operation = line.split(" ")[0]
        args = ARGUMENTS.findall(line)
        new_args = []
        if args:
            args = args[0].split(", ")
            for arg in args:
                if arg in labels:
                    new_args.append(str(labels[arg]))
                else:
                    new_args.append(arg)
        new_code.append(operation + " " + ", ".join(new_args))

    return new_code


def load_file(filename: str, log_level: int = logging.WARNING):
    """
    Parses and loads a file into memory

    :param log_level: The log level for the parser
    :param filename: The name of the file to load
    """
    parser = Parser(log_level)
    with open(filename) as f:
        processed_file = preprocess_code(list(map(lambda x: x.strip(), f.readlines())))
    statements = parser.parse_list(processed_file)

    for statement in statements:
        if statement.operation == TOKENS["ANCHOR"]:
            MEMORY.memory_counter = statement.arguments[0]
        else:
            val = MemoryValue()
            val.statement = statement
            MEMORY.insert_value(val)


def run():
    """
    Runs the program currently loaded into memory
    """
    logger = logging.getLogger("Interpreter")
    while MEMORY.pc.value <= MEMORY.get_max_address():
        current_pc = MEMORY.pc.value
        try:
            value = MEMORY.get_value_at_address(current_pc)
        except KeyError:
            break
        logger.debug(f"{value.statement.operation} {value.statement.arguments}")
        value.statement.execute()

        if MEMORY.pc.value == current_pc:
            MEMORY.pc.value += 1
