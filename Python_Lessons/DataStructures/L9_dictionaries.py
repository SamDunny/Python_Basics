# Python Dictionaries:
#   * Dictionaries is the 2nd of 4 built-in data structures
#   * Dictionaries are non-ordered (items do not have defined 'order', have key-value access)
#   * Dictionaries are changeable (you can add, remove, and change key-values in a dictionary)
#   * Dictionaries do not allow duplicate keys (can have duplicate values)
#   * Dictionaries must have immutable-type keys (the key cannot be changed, but the value can)

def histogram():
    # defualt dictionary
    counts = dict()
    # list of names
    names = ['Sam', 'Ali', 'Riley', 'Jack', 'Riley', 'Jack', 'Ali', 'Riley', 'Jack', 'Sam', 'Ali', 'Riley']

    # forloop to loop through all the names
    for name in names:
        # gets current count for the name (or 0 for new name)
        # adds 1 to the count
        # adds entry to counts dictionary
        counts[name] = counts.get(name, 0) + 1
    print(counts)

def main():
    # create a default dictionary
    classes = dict()

    # creating [key] = value pairs (automatically added to dict)
    classes['CSCE492'] = "Capstone 2"
    classes['CSCE416'] = "Networking"
    classes['ELCT371'] = "Electronics"
    classes['CSCE390'] = "Issues"

    # print dictionary
    print("Classes Dictionary: \n" + str(classes))

    # modify a dictionary entry with a given key
    classes['CSCE416'] = "Intro to " + classes['CSCE416']
    print("\nModified classes: \n" + str(classes))

    # creating a parameterized dictionary (dictionary literals)
    patterns = {'green':'go', 'yellow':'slow', 'red':'stop'}

    # using a forloop to create a numbered dictionary (essentially a list)

    # another way of constructing a default dictionary
    fake_list = {}
    # print(type(fake_list))
    index_num = 8
    for i in range(10):
        fake_list[i] = "Entry #: " + str(i)

    # can use forloop to iterate through dictionary by keys
    # for key in fake_list:
    #     print(key, fake_list[key])

    print("\nPsuedo-List: " + str(fake_list))
    # can print a dictionary by 'index'
    print("Psuedo-List at " + str(index_num) + ": " + str(fake_list[index_num]))

    # using the get method
    ages = {'Alice':30, 'Bob':35, 'Carol':12}
    # if the person youre looking for is in the dict, return their age
    #   if "Debbie" in ages:
    #       temp = ages["Debbie"]
    #   else:
    #       temp = -1
    # the above get is equal to .get()

    temp = ages.get("Debbie", -1)
    print("\n" + str(temp))
    temp = ages.get("Alice", -1)
    print(temp)
    print(ages)

    # print out all methods for dictionaries
    print("\nDictionary Methods:")
    # creating default dictionary
    x = dict()
    for methods in dir(x):
        print(methods)

    # run the histogram function example to observe dictionaries and .get()
    print("\nRunning the histogram example")
    histogram()

if __name__ == "__main__":
    main()