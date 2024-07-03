from Command.ICommand import ICommand

class StopServerCommand(ICommand):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.stop()