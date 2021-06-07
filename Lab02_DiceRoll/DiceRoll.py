# by Sam Dunny

import random

def main():
    # roll amount prompt
    roll_amt = int(input("Enter the number of times a 6 sided die should be rolled\n"))    
    if (roll_amt <= 0):
        while(roll_amt <= 0):
            roll_amt = int(input("INVALID VALUE, Enter the number of times a 6 sided die should be rolled\n"))

    # count variables
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    # for loop from 0 to roll_amt-1
    for i in range(roll_amt):
        # pick a random from 1 to 6
        roll = random.randrange(6) + 1

        # track variable counts
        if (roll == 1):
            ones+=1
        elif (roll == 2):
            twos+=1
        elif (roll == 3):
            threes+=1
        elif (roll == 4):
            fours+=1
        elif (roll == 5):
            fives+=1
        elif (roll == 6):
            sixes+=1
        else:
            print("ROLL ERROR: " + str(roll))

        # report current roll
        print("Roll " + str(i + 1) + ": " + str(roll) + " was rolled")

    # report roll stats
    print("\nCount Statistics:")
    print("One: " + str(ones) +
          "\nTwo: " + str(twos) +
          "\nThree: " + str(threes) +
          "\nFour: " + str(fours) +
          "\nFive: " + str(fives) + 
          "\nSix: " + str(sixes))

# run the main function
if __name__ == "__main__":
    main()