import threading
import time
from queue import Queue
from threading import Thread


class Action(object):
    def __init__(self, action=None, *args, **kwargs):
        self.name = None
        self.__action__ = None
        self.__args__ = None
        self.__kwargs__ = None
        self.set(action, *args, **kwargs)

    def set(self, action, *args, **kwargs):
        self.name = action.__name__
        self.__action__ = action
        self.__args__ = args
        self.__kwargs__ = kwargs

    def run(self):
        self.__action__.__call__(*self.__args__, **self.__kwargs__)

class DyThread(object):
    def __init__(self, name=None, daemon=False):
        self.name = name
        self.__actions__ = Queue()
        self.thread = Thread(target=self.thread_loop, daemon=daemon)

        if self.name is not None:
            self.thread.setName(self.name)

        self.is_new = True

    def thread_loop(self):
        while True:
            if not self.__actions__.empty():
                self.is_new = False
                action = self.__actions__.get_nowait()

                if action is None:
                    break

                action.run()
            else:
                pass
                # self.thread.setDaemon(True)

    def start(self):
        self.thread.start()

    def restart(self):
        daemon = self.thread.daemon
        self.thread = Thread(target=self.thread_loop, daemon=daemon, name=self.name)
        self.start()

    def stop(self):
        self.addAction(None)

    def join(self):
        self.thread.join()

    def addAction(self, action):
        self.__actions__.put_nowait(action)


if __name__ == '__main__':

    class App(object):
        def __init__(self):
            print("First thread: " + str(threading.get_ident()))

            self.main_thread = DyThread(name="main")
            self.sub_thread = DyThread(name="sub", daemon=True)

            main_action = Action(self.addActionsToThread, self.main_thread)
            self.main_thread.addAction(main_action)

            self.main_thread.start()
            # self.sub_thread.start()

            print("\nLast thread: " + str(threading.get_ident()))

            # while True:
            #     time.sleep(1)

        def addActionsToThread(self, thread: DyThread):
            print(f"{self.main_thread.name} id: {threading.get_ident()}")

            # time.sleep(0.1)

            count = 0
            while count < 3:
                count += 1
                thread.addAction(Action(self.printTest, thread, count))
                time.sleep(1)

            # self.sub_thread.stop()

            print(threading.enumerate())

            self.main_thread.stop()

        def printTest(self, thread, num):
            thread_name = thread.name
            print(f"{thread_name} id: {threading.get_ident()}")
            print(f"{thread_name}: {num}")
            # sleep(5)

    app = App()

    time.sleep(5)
    print("-"*30)

    main_action = Action(app.addActionsToThread, app.main_thread)
    app.main_thread.addAction(main_action)
    app.main_thread.restart()
