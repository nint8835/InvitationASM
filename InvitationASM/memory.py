import typing
import logging

from . import parser


class MemoryValue(object):
    value = 0
    statement = None  # type: parser.Statement


class Memory(object):

    def __init__(self):
        """
        Initialize a new memory object
        """

        self.logger = logging.getLogger("Memory")

        self.r = MemoryValue()
        self.gt = MemoryValue()
        self.lt = MemoryValue()
        self.eq = MemoryValue()
        self.pc = MemoryValue()
        self.pc.value = 1

        self.memory_counter = 1
        self._values = {-1: self.r}  # type: typing.Dict[int, MemoryValue]

    def get_value_at_address(self, address) -> MemoryValue:
        """
        Gets the MemoryValue object contained at a certain memory address

        :param address: The address to get the value from
        :return: The MemoryValue at that address
        """
        self.logger.debug(f"Getting value from address {address}")
        return self._values[address]

    def insert_value(self, value: MemoryValue, address: int=None):
        """
        Inserts a MemoryValue into memory

        :param value: The memory value to insert
        :param address: The address to insert into (or None to insert at next available address)
        """
        if address is None:
            address = self.memory_counter
            self.memory_counter += 1

        self._values[address] = value
        self.logger.debug(f"Inserted value at address {address}")

    def set_value(self, value: int, address: int):
        """
        Sets the value of a memory location

        :param value: The value for it to be set to
        :param address: The location to set the value of
        """
        if address not in self._values:
            cell = MemoryValue()
            self.insert_value(cell, address)
        else:
            cell = self.get_value_at_address(address)
        cell.value = value

    def get_value(self, address: int) -> int:
        """
        Gets the value of a memory location

        :param address: The address to get the value of
        :return: The value at that address
        """

        if address not in self._values:
            self.insert_value(MemoryValue(), address)
            return 0
        else:
            return self.get_value_at_address(address).value

    def get_max_address(self) -> int:
        return max(self._values.keys())


MEMORY = Memory()
