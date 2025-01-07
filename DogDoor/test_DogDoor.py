import pytest
from Remote import Remote
from DogDoor import DogDoor
from BarkRecognizer import BarkRecognizer
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

def test_bark_recognizer():
    door = DogDoor()
    remote = Remote(door)
    bark = BarkRecognizer(door)
    bark.set_allowed_bark("Woff")
    bark.recognize("Woff")
    assert door.isOpen() == True

def test_bark_recognizer():
    door = DogDoor()
    remote = Remote(door)
    bark = BarkRecognizer(door)
    bark.set_allowed_bark("Woff")
    bark.recognize("Wofffff")
    assert door.isOpen() == False


if __name__ == "__main__":
    pytest.main()
