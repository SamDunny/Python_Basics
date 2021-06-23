# must import the regex lib to use regex functions
import re

def main():
    fileName = 'exemail.txt'
    try:
        fhand = open(fileName)
    except:
        print("\nFile cannot be opened: " + fileName)
        quit()

    for line in fhand:
        line = line.rstrip()
        # searches for lines that start(^) with from: or start(^) with subject
        if re.search('^from:', line) or re.search('^subject:', line):
            print(line)

    test_line = 'Its 5 deg in Alaska, 90 deg in South Dakota, and 110 deg in South Carolina'
    # finds all occurances of the numbers 0-9 that happen 1 or more times
    test_result = re.findall('[0-9]+', test_line)
    print('\n',test_result)

if __name__ == "__main__":
    main()