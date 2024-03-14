from Guitar import Guitar


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

    def search(self, guitar_input: Guitar):
        result = []
        for guitar in self.guitars:
            if guitar.get_manufacturer() != guitar_input.get_manufacturer():
                continue
            if guitar.get_back_material() != guitar_input.get_back_material():
                continue
            result.append(guitar)
        return result
