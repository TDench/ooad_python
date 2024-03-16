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

    def search(self, wanted_spec:GuitarSpec):
        result = []
        for guitar in self.guitars:
            guitar_spec = guitar.get_spec()
            if guitar_spec.get_manufacturer() != wanted_spec.get_manufacturer():
                continue
            if guitar_spec.get_back_material() != wanted_spec.get_back_material():
                continue
            result.append(guitar)
        return result
