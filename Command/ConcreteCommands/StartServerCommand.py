from Command.ICommand import ICommand

class StartServerCommand(ICommand):
    def __init__(self, server):
        self.server = server

    def execute(self):
        self.server.start()