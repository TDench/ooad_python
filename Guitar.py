class Guitar:
    def __init__(self, price, id, manufacturer, back_material):
        self.price = price
        self.id = id
        self.manufacturer = manufacturer
        self.back_material = back_material

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def get_manufacturer(self):
        return self.manufacturer

    def get_back_material(self):
        return self.back_material
