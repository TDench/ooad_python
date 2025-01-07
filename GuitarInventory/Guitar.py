class Guitar:
    def __init__(self, price, id, spec):
        self.price = price
        self.id = id
        self.spec = spec

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def get_spec(self):
        return self.spec


class GuitarSpec:
    def __init__(self, manufacturer, back_material, num_strings):
        self.manufacturer = manufacturer
        self.back_material = back_material
        self.num_strings = num_strings

    def get_manufacturer(self):
        return self.manufacturer

    def get_back_material(self):
        return self.back_material

    def get_num_strings(self):
        return self.num_strings

    def matches(self, other):
        if other.get_manufacturer() is not None:
            if other.get_manufacturer() != self.get_manufacturer():
                return False

        if other.get_back_material() is not None:
            if other.get_back_material() != self.get_back_material():
                return False

        if other.get_num_strings() is not None:
            if other.get_num_strings() != self.get_num_strings():
                return False

        return True
