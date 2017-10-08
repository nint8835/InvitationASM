from .exceptions import OperationDeclarationException

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


class ExampleOperation(metaclass=Operation):
    TOKEN = "EXMP"
    OPCODE = 48

    def execute(self, args):
        pass
