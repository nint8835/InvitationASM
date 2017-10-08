import abc

TOKENS = {}
OPCODES = {}


class Operation(type):

    def __init__(cls, name, bases, dct):
        TOKENS[dct["TOKEN"]] = cls()
        OPCODES[dct["OPCODE"]] = TOKENS[dct["TOKEN"]]
        super().__init__(name, bases, dct)


class ExampleOperation(metaclass=Operation):
    TOKEN = "EXMP"
    OPCODE = 48
