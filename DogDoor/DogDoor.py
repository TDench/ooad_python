import time
import threading


class DogDoor:
    def __init__(self) -> None:
        self.__open = False

    def open(self):
        print("Door is open")
        self.__open = True
        threading.Thread(target=self.auto_close).start()

    def close(self):
        print("Door is closed")
        self.__open = False

    def isOpen(self):
        return self.__open

    def auto_close(self):
        print("start audo close")
        time.sleep(3)
        print("autoclose door")
        self.close()
