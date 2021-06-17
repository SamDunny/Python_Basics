# Python Lists:
#   * Lists is the 1st of 4 built-in data structures
#   * Lists are ordered (items have defined 'order' because of indexing)
#   * Lists are changeable (you can add, remove, and change items in a list)
#   * Lists allow duplicate values (because theyre ordered)

def main():
    l1 = [1,2,3]
    l2 = [4,5,6]
    print("List 1: " + str(l1))
    print("List 2: " + str(l2))

    # list concatenation
    l3 = l1 + l2
    print("\nList 3 (concat): " + str(l3))

    # list slicing ([X,Y] starts at X 'inclusive', goes up to but not including Y 'exclusive')
    i1 = 1
    i2 = 3
    i3 = 10
    print("Slicing from index " + str(i1) + " to " + str(i2) + ": "+ str(l3[i1:i2]))
    print("Slicing from index " + str(i2) + " to " + str(i3) + ": "+ str(l3[i2:i3]))

    # print out all methods for lists
    print("\nList Methods:")
    # creating default list
    x = list()
    for methods in dir(x):
        print(methods)

    # using the split method to pull apart an email header
    fileName = 'exemail.txt'
    # opening file handle that reads in exemail.txt
    try:
        fhand = open(fileName)
    except:
        print("\nFile cannot be opened: " + fileName)
        quit()
    # will read the entire file to one string variable
    inp = fhand.read()

    # will split email on space delimiter
    emailText = inp.split()

    # print("\n" + str(emailText))
    print("\nSender: " + str((emailText[2].split('@'))[0]))
    print("Recipient: " + str((emailText[6].split('@'))[0]))

if __name__ == "__main__":
    main()