import pytest
from .Remote import Remote
from .DogDoor import DogDoor
from .BarkRecognizer import BarkRecognizer
from .Bark import Bark
import time


def test_door_open_taggle():
    door = DogDoor()
    remote = Remote(door)
    assert door.isOpen() == False
    remote.press_button()
    assert door.isOpen() == True
    remote.press_button()
    assert door.isOpen() == False


def test_door_auto_close():
    door = DogDoor()
    remote = Remote(door)
    assert door.isOpen() == False
    remote.press_button()
    assert door.isOpen() == True
    time.sleep(1.1)
    assert door.isOpen() == False


def test_door_auto_close_and_open():
    door = DogDoor()
    remote = Remote(door)
    assert door.isOpen() == False
    remote.press_button()
    assert door.isOpen() == True
    time.sleep(1.1)
    assert door.isOpen() == False


def test_bark_recognizer_same():
    door = DogDoor()
    bark = Bark("Woff")
    door.set_allowed_bark(bark)
    bark_recognizer = BarkRecognizer(door)
    assert door.isOpen() == False
    bark_recognizer.recognize(bark)
    assert door.isOpen() == True


def test_bark_recognizer_different():
    door = DogDoor()
    bark = Bark("Woff")
    bark_yip = Bark("Yipss")
    door.set_allowed_bark(bark)
    bark_recognizer = BarkRecognizer(door)
    assert door.isOpen() == False
    bark_recognizer.recognize(bark_yip)
    assert door.isOpen() == False


if __name__ == "__main__":
    pytest.main()
