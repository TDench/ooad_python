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
    def __init__(self, manufacturer, back_material):
        self.manufacturer = manufacturer
        self.back_material = back_material

    def get_manufacturer(self):
        return self.manufacturer

    def get_back_material(self):
        return self.back_material