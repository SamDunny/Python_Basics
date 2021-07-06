from Fruit import Fruit

NAMES = ['Granny', 'Red', 'Gala', 'Yellow']

# Apple class inherits from Fruit class
class Apple(Fruit):
    # instance variables
    name = ""
    hasWorms = False

    # default type
    DEF_name = "Red"
    DEF_hasWorms = False

    # initialize apple
    def __init__(self, aWeight, aPrice, aName, hasWorms):
        # call parents constructor
        super().__init__("Apple", aWeight, aPrice)
        self.setName(aName)
        self.setHasWorms(hasWorms)

    # mutators
    def setName(self, aName):
        if aName not in NAMES:
            print("Invalid Apple name, setting default: ", self.DEF_name)
            self.name = self.DEF_name
        else:
            self.name = aName
    def setHasWorms(self, cond):
        if cond == True: hasWorms = True
        elif cond == False: hasWorms = False
        else: print("Error: non-bool value: ", cond)

    def toString(self):
        Fruit.toString(self)
        print("Name:\t", self.name)
        print("Worms:\t", self.hasWorms)