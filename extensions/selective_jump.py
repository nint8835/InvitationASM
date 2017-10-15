from InvitationASM.operations import Operation
from InvitationASM.memory import MEMORY


class SJumpOperation(metaclass=Operation):
    TOKEN = "SJUMP"

    def execute(self, arguments):
        pairs = zip(arguments[1::2], arguments[2::2])
        val = MEMORY.get_value(arguments[0])

        for pair in pairs:
            if pair[0] == val:
                MEMORY.pc.value = pair[1]
