from AppPackage.Experiments.Backend.AutoPrintServer.SocketManagers import ClientConnectivityManager


class AutoPrintDesktopClient(object):
    def __init__(self):
        self.connManager = ClientConnectivityManager(host='192.168.0.125', port=9999)


if __name__ == '__main__':
    AutoPrintDesktopClient()
