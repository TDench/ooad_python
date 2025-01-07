from Guitar import GuitarSpec


class Inventory:
    def __init__(self):
        self.guitars = []

    def addGuitar(self, guitar):
        self.guitars.append(guitar)

    def get_guitar(self, id):
        for guitar in self.guitars:
            if id == guitar.get_id():
                return guitar
        return None

    def search(self, wanted_spec: GuitarSpec):
        result = []
        for guitar in self.guitars:
            guitar_spec = guitar.get_spec()
            if guitar_spec.matches(wanted_spec):
                result.append(guitar)
        return result
