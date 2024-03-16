import pytest
from Remote import Remote
import time


def test_door_open_taggle():
    remote = Remote()
    assert remote.door.isOpen() == False
    remote.press_button()
    assert remote.door.isOpen() == True
    remote.press_button()
    assert remote.door.isOpen() == False


def test_door_auto_close():
    remote = Remote()
    assert remote.door.isOpen() == False
    remote.press_button()
    assert remote.door.isOpen() == True
    time.sleep(3.1)
    assert remote.door.isOpen() == False


def test_door_auto_close_and_open():
    remote = Remote()
    assert remote.door.isOpen() == False
    remote.press_button()
    assert remote.door.isOpen() == True
    time.sleep(3.1)
    assert remote.door.isOpen() == False
    remote.press_button()
    assert remote.door.isOpen() == True


if __name__ == "__main__":
    pytest.main()
