class Bark:
    def __init__(self, sound: str):
        self.sound = sound

    def getSound(self) -> str:
        return self.sound

    def equals(self, other) -> bool:
        if isinstance(other, Bark):
            return self.sound == other.getSound()
        return False
