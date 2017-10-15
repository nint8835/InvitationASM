from InvitationASM.operations import Operation


class UOutOperation(metaclass=Operation):
    TOKEN = "UOUT"

    def execute(self, arguments):
        print("".join(map(chr, arguments)))
