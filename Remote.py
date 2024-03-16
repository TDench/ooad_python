from DogDoor import DogDoor


class Remote:
    def __init__(self) -> None:
        self.door = DogDoor()

    def press_button(self):
        print("Pressing the bottom")

        if self.door.isOpen():
            self.door.close()
        else:
            self.door.open()
