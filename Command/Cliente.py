from ConcreteCommands.RestartServerCommand import RestartServerCommand
from ConcreteCommands.StartServerCommand import StartServerCommand
from ConcreteCommands.StopServerCommand import StopServerCommand
from Receiver.Server import Server
from Invoker.RemoteControl import RemoteControl

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
