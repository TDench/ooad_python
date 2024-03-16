import pytest
from Remote import Remote


def test_add_guitar():
    remote = Remote()
    assert remote.door.isOpen() == False
    remote.press_button()
    assert remote.door.isOpen() == True
    remote.press_button()
    assert remote.door.isOpen() == False
