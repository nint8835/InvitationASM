import typing

from . import parser


class MemoryValue(object):
    value = 0
    statement = None  # type: parser.Statement


class Memory(object):

    def __init__(self):
        
        self.r = MemoryValue()
        self.gt = MemoryValue()
        self.lt = MemoryValue()
        self.eq = MemoryValue()

        self._memory_counter = 0
        self._values = {}  # type: typing.Dict[int, MemoryValue]

    def get_value_at_address(self, address) -> MemoryValue:
        return self._values[address]

    def insert_value(self, value: MemoryValue, address: int=None):
        if address is None:
            address = self._memory_counter
            self._memory_counter += 1

        self._values[address] = value


MEMORY = Memory()
