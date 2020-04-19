import socket
from _thread import start_new_thread
from threading import Thread


class ConnectivityManager(object):
    def __init__(self, host="", port=9999):
        self.socket: socket.socket = None

        self.host = host
        self.port = port

        self.setupSocket()

    def setupSocket(self):
        pass

    def _createSocket(self):
        try:
            self.socket = socket.socket()
            print("Socket has been created.")

        except socket.error as msg:
            print("Socket creation error: " + str(msg))

    def sendMessage(self, message: str):
        self.socket.send(message.encode("utf-8"))

class ClientConnectivityManager(ConnectivityManager):
    def __init__(self, host="", port=9999):
        super(ClientConnectivityManager, self).__init__(host=host, port=port)

    def setupSocket(self):
        self._createSocket()
        self._connectSocket()
        Thread(target=self.listenToServer).start()

    def listenToServer(self):
        while True:
            try:
                data = self.socket.recv(2048)

            except ConnectionResetError:
                continue

            message = str(data.decode("utf-8"))
            print("Server: " + message)
            self.onResponse(message)

        # self._closeConnection(conn_full_address)

    def _connectSocket(self):
        self.socket.connect((self.host, self.port))

    def onResponse(self, response):
        pass

class ServerConnectivityManager(ConnectivityManager):

    def __init__(self, host="", port=9999):
        self.connections = {}
        super(ServerConnectivityManager, self).__init__(host=host, port=port)

    def listenToConnections(self):
        while True:
            self._acceptConnection()

    def listenToClient(self, conn_full_address):
        connection = self.connections[conn_full_address]
        while True:
            try:
                data = connection.recv(2048)
                if not data:
                    break

            except ConnectionResetError:
                break

            message = str(data.decode("utf-8"))
            print(f"Client {conn_full_address}: " + message)
            self.onMessageReceived(message)

        self._closeConnection(conn_full_address)

    def setupSocket(self):
        self._createSocket()
        self._bindSocket()
        self.socket.setblocking(True)
        Thread(target=self.listenToConnections).start()

    def onMessageReceived(self, message):
        pass

    def _bindSocket(self):
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            print("Socket has been bonded.")

        except socket.error as msg:
            print("Socket Binding error" + str(msg) + "\n" + "Retrying...")

    def _acceptConnection(self):
        try:
            conn, address = self.socket.accept()
            full_address = ":".join([str(item) for item in address])
            self.connections[full_address] = conn
            print(f"Connection has been established: \"{full_address}\"")

            start_new_thread(self.listenToClient, (full_address,))

        except socket.error as msg:
            print("Socket acceptance error: " + str(msg))

    def _closeConnection(self, conn_full_address):
        print(f"Client \"{conn_full_address}\" is disconnected.")
        self.connections[conn_full_address].close()
        del self.connections[conn_full_address]
