from DogDoor import DogDoor
import time
import threading


class Remote:
    def __init__(self) -> None:
        self.door = DogDoor()

    def press_button(self):
        print("Pressing the bottom")

        if self.door.isOpen():
            self.door.close()
        else:
            self.door.open()
            threading.Thread(target=self.auto_close).start()

    def auto_close(self):
        print("start audo close")
        time.sleep(3)
        print("autoclose door")
        self.door.close()
        
