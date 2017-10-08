from .exceptions import OperationDeclarationException
from .memory import MEMORY

TOKENS = {}
OPCODES = {}


class Operation(type):

    def __init__(cls, name, bases, dct):
        if "TOKEN" in dct:
            if dct["TOKEN"] not in TOKENS:
                TOKENS[dct["TOKEN"]] = cls()
            else:
                raise OperationDeclarationException(f"Operation token {dct['TOKEN']} already in use")
        else:
            raise OperationDeclarationException("Operation must have TOKEN attribute")

        if "OPCODE" in dct:
            if dct["OPCODE"] not in OPCODES:
                OPCODES[dct["OPCODE"]] = TOKENS[dct["TOKEN"]]
            else:
                raise OperationDeclarationException(f"Operation opcode {dct['OPCODE']} already in use")
        else:
            raise OperationDeclarationException("Operation must have OPCODE attribute")

        if "execute" not in dct:
            raise OperationDeclarationException("Operation must declare execute method")

        super().__init__(name, bases, dct)


class LoadOperation(metaclass=Operation):
    TOKEN = "LOAD"
    OPCODE = 1

    def execute(self, arguments):
        MEMORY.r.value = arguments[0]


class PrintOperation(metaclass=Operation):
    TOKEN = "PRINT"
    OPCODE = 2

    def execute(self, arguments):
        print(MEMORY.get_value_at_address(arguments[0]).value)
