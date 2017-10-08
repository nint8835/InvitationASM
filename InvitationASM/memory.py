import typing
import logging

from . import parser


class MemoryValue(object):
    value = 0
    statement = None  # type: parser.Statement


class Memory(object):

    def __init__(self):

        self.logger = logging.getLogger("Memory")

        self.r = MemoryValue()
        self.gt = MemoryValue()
        self.lt = MemoryValue()
        self.eq = MemoryValue()
        self.pc = MemoryValue()

        self._memory_counter = 0
        self._values = {}  # type: typing.Dict[int, MemoryValue]

    def get_value_at_address(self, address) -> MemoryValue:
        self.logger.debug(f"Getting value from address {address}")
        return self._values[address]

    def insert_value(self, value: MemoryValue, address: int=None):
        if address is None:
            address = self._memory_counter
            self._memory_counter += 1

        self._values[address] = value
        self.logger.debug(f"Inserted value at address {address}")

    def get_max_address(self) -> int:
        return max(self._values.keys())


MEMORY = Memory()
