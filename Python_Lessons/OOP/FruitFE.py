from Fruit import Fruit
from Apple import Apple

# main class
class FruitFE():

    # main method
    def main():
        # create fruit
        fr1 = Fruit("Pear", 3.0, 3.0)
        fr1.toString()
        print()

        # create a parametrized apple
        ap1 = Apple(5.0, 2.0, 'Gala', False)
        ap1.toString()
        

if __name__ == '__main__':
    FruitFE.main()