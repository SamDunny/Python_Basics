# Python Tuple:
#   * Tuples is the 3rd of 4 built-in data structures
#   * Tuples are essentially immutable lists
#   * Tuples are ordered (items have defined 'order' because of indexing)
#   * Tuples are unchangeable (you cannot add, remove, or change items in a tuple (unless that item is mutebable))
#   * Tuples allow duplicate values (because theyre ordered)

def main():
    # tuples allow for multiple assignment
    (x,y,z) = (0,1,2)

    # tuples can allow for multiple variable tracking in a for loop
    d = dict()

    d["rock"] = "hard"
    d["pillow"] = "soft"
    d["clay"] = "medium"

    for (k,i) in d.items():
        print(k,i)

    print()
    t = tuple()
    for methods in dir(t):
        print(methods)

    # you can add tuples together to form another tuple
    ex1 = (1,2,3)
    ex2 = (4,5,6)
    ex1 = ex1 + ex2
    print("\n",ex1)

    # sorts dictionary based on key values
    t = sorted(d.items())

    # prints out the key and value from the sorted list
    for k,v in t:
        print(k,"\t", v)

    print()
    d = {'a':12, 'b':78, 'c':3, 'd':96}
    temp = list()

    # reverse key and value in temp list
    for k,v in d.items():
        temp.append((v, k))

    print("Dictionary:\t\t", d)
    print("List of Tuples(rev): \t", temp)

    # sort reversed key-value temp list by keys (were previously values)
    temp = sorted(temp)
    print("Ascending:\t", temp)
    temp = sorted(temp, reverse=True)
    print("Descending:\t", temp)

    # use list comprehension and lambda functions to sort and print tuples from dicts
    l_dict = {'a':10, 'b':89, 'c':2}
    print("\n", sorted( [ (v,k) for k,v in l_dict.items() ] ))

if __name__ == "__main__":
    main()