from commands import StartServerCommand, StopServerCommand, RestartServerCommand
from server import Server
from rc import RemoteControl

server = Server()
start_command = StartServerCommand(server)
stop_command = StopServerCommand(server)
restart_command = RestartServerCommand(server)
remote = RemoteControl()

remote.set_command(start_command)
remote.press_button()

remote.set_command(stop_command)
remote.press_button()

remote.set_command(restart_command)
remote.press_button()
