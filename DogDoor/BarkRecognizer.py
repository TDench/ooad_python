from DogDoor import DogDoor


class BarkRecognizer:
    def __init__(self, door: DogDoor) -> None:
        self.__door = door
        self.__allowed_bark = ""

    def set_allowed_bark(self,bark:str):
        self.__allowed_bark = bark

    def get_allowed_bark(self):
        return self.__allowed_bark

    def recognize(self, bark: str):
        print(f"BarkRecongnizer heard {bark}")
        if self.get_allowed_bark() == bark:
            self.__door.open()
