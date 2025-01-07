import time
import threading
from .Bark import Bark


class DogDoor:
    def __init__(self) -> None:
        self.__open = False
        self.__allowed_bark = None

    def open(self) -> None:
        print("Door is open")
        self.__open = True
        threading.Thread(target=self.auto_close).start()

    def close(self) -> None:
        print("Door is closed")
        self.__open = False

    def isOpen(self) -> bool:
        return self.__open

    def auto_close(self) -> None:
        print("start audo close")
        time.sleep(1)
        print("autoclose door")
        self.close()

    def set_allowed_bark(self, bark: Bark) -> None:
        self.__allowed_bark = bark

    def get_allowed_bark(self) -> Bark:
        return self.__allowed_bark
