# Każda z klas dziedziczących ma mieć zaimplementowaną metodę
# __str__ , która będzie opisywała obiekt.
# Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas
# tworzenia instancji klasy za pośrednictwem konstruktora.
# Stworzyć po jednym obiekcie klasy House oraz Flat, a następnie je
# wyświetlić.


class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}."
class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"Plot: {self.plot}, area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}."


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Floor: {self.floor}, area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}."


house = House(155, 6, 1500000, "Leśna 53", 300)
flat = Flat(88, 4, 900000, "Polna 15", 3)
print(house)
print(flat)
