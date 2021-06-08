# by Sam Dunny

# main function
def main():
    print("Welcome to the below average temperature tester program.")

    # number of days we are tracking
    numOfDays = 5
    tempAvg = 0.0
    tempTot = 0.0

    # initialize empty temperature list
    tempList = []

    for i in range(numOfDays):
        temp = float(input("Please enter the temperature for day " + str(i+1) + "\n"))
        # tempList[i] = temp
        tempList.append(temp)
        tempTot+=temp

    tempAvg = tempTot/float(numOfDays)

    print("The average temperature was " + str(tempAvg))

    print("\nThe days that were below average were")
    for i in range(numOfDays):
        if tempList[i] < tempAvg:
            print("Day " + str(i+1) + " with " + str(tempList[i]))


# run the main function
if __name__ == "__main__":
    main()