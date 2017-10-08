import typing


class MemoryValue(object):
    address = 0
    operation = None
    arguments = []


class Memory(object):

    def __init__(self):
        self.r = 0
        self._memory_counter = 0
        self._values = {}  # type: typing.Dict[int, MemoryValue]

    def get_value_at_address(self, address) -> MemoryValue:
        return self._values[address]

    def insert_value(self, value: MemoryValue, address: int=None):
        if address is None:
            address = self._memory_counter
            self._memory_counter += 1

        self._values[address] = value
