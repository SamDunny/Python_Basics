# list of valid names
TYPES = ['Apple', 'Pear', 'Tomato', 'Orange']

class Fruit():
    # instance variables
    type = ""
    weight = 0.0
    price = 0.0

    # default values
    DEF_type = "Apple"
    DEF_weight = 0.001
    DEF_price = 0.01

    # parameterized constructor
    def __init__(self, aType, aWeight, aPrice):
        self.setaType(aType)
        self.setaWeight(aWeight)
        self.setaPrice(aPrice)

    # mutators
    def setaType(self, aType):
        if aType not in TYPES:
            print("Invalid Fruit type, setting default: ", self.DEF_type)
            self.type = self.DEF_type
        else:
            self.type = aType
    def setaWeight(self, aWeight):
        if aWeight <= 0.0:
            print("Invalid Fruit weight, setting default: ", self.DEF_weight)
            self.weight = self.DEF_weight
        else:
            self.weight = aWeight
    def setaPrice(self, aPrice):
        if aPrice <= 0.0:
            print("Invalid Fruit price, setting default: ", self.DEF_price)
            self.price = self.DEF_price
        else:
            self.price = aPrice

    # bite method
    def bite(self):
        if self.weight > 0.0:
            self.weight -= 0.5
        else:
            print("Fruit has been eaten")

    # toString method
    def toString(self):
        print("Type:\t", self.type)
        print("Weight:\t", self.weight)
        print("Price:\t", self.price)