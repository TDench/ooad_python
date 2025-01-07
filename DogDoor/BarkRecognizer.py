from .DogDoor import DogDoor
from .Bark import Bark


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door

    def recognize(self, bark: Bark):
        print(f"BarkRecongnizer heard {bark.getSound()}")
        if self.__door.get_allowed_bark().equals(bark):
            self.__door.open()
        else:
            print("this do is not allowed")
