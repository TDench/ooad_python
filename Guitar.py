class Guitar:
    def __init__(self, price, number, manufacturer, back_material):
        self.price = price
        self.number = number
        self.manufacturer = manufacturer
        self.back_material = back_material

    def get_price(self):
        return self.price

    def get_number(self):
        return self.number

    def get_manufacturer(self):
        return self.manufacturer

    def get_back_material(self):
        return self.back_material
