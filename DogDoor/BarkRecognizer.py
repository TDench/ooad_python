from .DogDoor import DogDoor
from .Bark import Bark


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door
        self.__allowed_bark = ""

    def set_allowed_bark(self, bark: str):
        self.__allowed_bark = bark

    def get_allowed_bark(self):
        return self.__allowed_bark

    def recognize(self, bark: Bark):
        print(f"BarkRecongnizer heard {bark.getSound()}")
        allowed_barks = self.__door.get_allowed_barks()
        for allowed_bark in allowed_barks:
            if allowed_bark.equals(bark):
                self.__door.open()
            else:
                print("this do is not allowed")
