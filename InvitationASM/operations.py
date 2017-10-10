from .exceptions import OperationDeclarationException
from .memory import MEMORY, MemoryValue

TOKENS = {}


class Operation(type):

    def __init__(cls, name, bases, dct):
        if "TOKEN" in dct:
            if dct["TOKEN"] not in TOKENS:
                TOKENS[dct["TOKEN"]] = cls()
            else:
                raise OperationDeclarationException(f"Operation token {dct['TOKEN']} already in use")
        else:
            raise OperationDeclarationException("Operation must have TOKEN attribute")

        if "execute" not in dct:
            raise OperationDeclarationException("Operation must declare execute method")

        super().__init__(name, bases, dct)


class LoadOperation(metaclass=Operation):
    TOKEN = "LOAD"

    def execute(self, arguments):
        MEMORY.r.value = MEMORY.get_value_at_address(arguments[0]).value


class PrintOperation(metaclass=Operation):
    TOKEN = "PRINT"

    def execute(self, arguments):
        print(f"{arguments[0]} -> {MEMORY.get_value_at_address(arguments[0]).value}")


class CompareOperation(metaclass=Operation):
    TOKEN = "COMPARE"

    def execute(self, arguments):
        value1 = MEMORY.get_value_at_address(arguments[0]).value
        value2 = MEMORY.get_value_at_address(arguments[1]).value
        MEMORY.gt.value = int(value1 > value2)
        MEMORY.lt.value = int(value1 < value2)
        MEMORY.eq.value = int(value1 == value2)


class StoreOperation(metaclass=Operation):
    TOKEN = "STORE"

    def execute(self, arguments):
        try:
            value = MEMORY.get_value_at_address(arguments[0])
        except KeyError:
            value = MemoryValue()
            MEMORY.insert_value(value, arguments[0])
        value.value = MEMORY.r.value


class InitOperation(metaclass=Operation):
    TOKEN = "INIT"

    def execute(self, arguments):
        value = MemoryValue()
        value.value = arguments[1]
        MEMORY.insert_value(value, arguments[0])


class JumpOperation(metaclass=Operation):
    TOKEN = "JUMP"

    def execute(self, arguments):
        MEMORY.pc.value = arguments[0]


class AddOperation(metaclass=Operation):
    TOKEN = "ADD"

    def execute(self, arguments):
        value = MEMORY.get_value_at_address(arguments[0]).value
        MEMORY.r.value += value


class MultiplyOperation(metaclass=Operation):
    TOKEN = "MULTIPLY"

    def execute(self, arguments):
        value = MEMORY.get_value_at_address(arguments[0]).value
        MEMORY.r.value *= value


class JumpGTOperation(metaclass=Operation):
    TOKEN = "JUMPGT"

    def execute(self, arguments):
        if MEMORY.gt.value == 1:
            MEMORY.pc.value = arguments[0]
