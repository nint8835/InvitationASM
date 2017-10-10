import logging

from .parser import Parser
from .operations import TOKENS
from .memory import MemoryValue, MEMORY


def load_file(filename: str, log_level: int = logging.WARNING):
    """
    Parses and loads a file into memory

    :param filename: The name of the file to load
    """
    parser = Parser(log_level)
    statements = parser.parse_file(filename)

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
