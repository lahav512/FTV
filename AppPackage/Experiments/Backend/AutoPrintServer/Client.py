from queue import Queue
from threading import Thread

from AppPackage.Experiments.Backend.AutoPrintServer.Commands import AutoPrintServerCommands
from AppPackage.Experiments.Backend.AutoPrintServer.SocketManagers import ClientConnectivityManager


Commands = AutoPrintServerCommands


class AutoPrintDesktopClient(object):

    def __init__(self):
        self.connManager = ClientConnectivityManager(host='192.168.0.125', port=9999)
        self.messages = Queue()
        self.setupClient()

    def setupClient(self):
        Thread(target=self.sendMessages).start()
        Thread(target=self.listenToUser).start()

    def sendMessage(self, message: str):
        self.connManager.sendMessage(message)

    def sendMessages(self):
        while True:
            if not self.messages.empty():
                msg = self.messages.get_nowait()
                func, data = msg.split(":", 1)

                data: str
                args = data.split("%", 1)

                if hasattr(self, func):
                    obj = getattr(self, func)
                    if callable(obj):
                        obj(args[0], args[1])
                        continue

                self.sendMessage(msg)

    def listenToUser(self):
        while True:
            msg = str(input("Send: "))
            self.addMessage(msg)

    def addMessage(self, message):
        self.messages.put(message)

    def sendCommand(self, cmd, data):
        self.sendMessage(f"{cmd}:{data}")

    def login(self, username, password):
        self.sendCommand(Commands.Server.login, "%".join([username, password]))

    def register(self, username, password):
        self.sendCommand(Commands.Server.register, "%".join([username, password]))


if __name__ == '__main__':
    AutoPrintDesktopClient()
