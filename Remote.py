from DogDoor import DogDoor



class Remote:
    def __init__(self,door:DogDoor) -> None:
        self.__door = door

    def press_button(self):
        print("Pressing the bottom")

        if self.__door.isOpen():
            self.__door.close()
        else:
            self.__door.open()