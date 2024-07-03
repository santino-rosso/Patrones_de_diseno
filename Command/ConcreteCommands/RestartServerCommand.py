from Command.ICommand import ICommand

class RestartServerCommand(ICommand):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.restart()
