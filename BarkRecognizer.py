from DogDoor import DogDoor
class BarkRecognizer:
    def __init__(self,door:DogDoor) -> None:
        self.__door = door
    
    def recognize(self,bark:str):
        print(f"BarkRecongnizer heard {bark}")
        self.__door.open()