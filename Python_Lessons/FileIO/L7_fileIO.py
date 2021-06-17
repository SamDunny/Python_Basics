def main():
    # variable for file name
    fileName = 'exemail.txt'

    # opening file handle that reads in exemail.txt
    try:
        fhand = open(fileName)
    except:
        print("File connot be opened: " + fileName)
        quit()
    print("Started processing on: " + fileName)

    # will read the entire file to one string variable
    inp = fhand.read()
    print("Characters in file: " + str(len(inp)))

    # resets file handle to beginning of file
    fhand.seek(0)

    # prints sender name
    for terms in fhand:
        # strips new line character off right hand side
        terms = terms.rstrip()
        if terms.startswith('from:'):
            print(terms)

    # resets file handle to beginning of file
    fhand.seek(0)
    
    print("FILE CONTENTS: \n")
    # printing out all text file date
    for terms in fhand:
        # strips new line character off right hand side
        terms = terms.rstrip()
        print(terms)

    print("Finished Processing")

if __name__ == "__main__":
    main()