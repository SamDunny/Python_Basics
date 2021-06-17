def main():
    counts = dict()

    # using the split method to pull apart an email header
    fileName = 'tears.txt'
    # opening file handle that reads in exemail.txt
    try:
        fhand = open(fileName)
    except:
        print("\nFile cannot be opened: " + fileName)
        quit()
    
    print("Reading " + fileName + "\n")
    # will read the entire file to one string variable
    inp = fhand.read()
    print(inp, "\n")

    # clean the input (replace all periods with empty space, trim whitespace off both sides, convert all letters to lowercase)
    inp = inp.replace(".","")
    inp = inp.replace(",","")
    inp = inp.replace("-","")
    inp = inp.replace("(","")
    inp = inp.replace(")","")
    inp.strip()
    inp = inp.lower()

    # test print the cleaned output
    # print(inp, "\n")

    # split the input string into words
    words = inp.split()

    # tally all counts
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # print the outcome
    # print('Counts', counts)

    bigCount = None
    bigWord = None
    # double forloop that keeps track of the double-tuple return from the .items() call
    for word,count in counts.items():
        if bigCount is None or count > bigCount:
            bigWord = word
            bigCount = count

    print("Most numerous word: ", bigWord, "\nCount: ", bigCount)

if __name__ == "__main__":
    main()