from .parser import Parser
from .memory import MemoryValue, MEMORY

parser = Parser()


def load_file(filename: str):
    statements = parser.parse_file(filename)

    for statement in statements:
        val = MemoryValue()
        val.statement = statement

        MEMORY.insert_value(val)


def run():
    while MEMORY.pc.value <= MEMORY.get_max_address():
        current_pc = MEMORY.pc.value
        try:
            value = MEMORY.get_value_at_address(current_pc)
        except KeyError:
            break
        value.statement.execute()

        if MEMORY.pc.value == current_pc:
            MEMORY.pc.value += 1
