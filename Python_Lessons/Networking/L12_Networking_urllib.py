# essentially, this lib reduces the complexity of ready urls to that of reading local text files
import urllib.request, urllib.parse, urllib.error

def main():
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())

if __name__ == '__main__':
    main()