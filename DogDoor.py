class DogDoor:
    def __init__(self) -> None:
        self.__open = False

    def open(self):
        print("Door is open")
        self.__open = True

    def close(self):
        print("Door is closed")
        self.__open = False

    def isOpen(self):
        return self.__open
