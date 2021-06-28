import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def print_HyperLinks(soup):
    # retrieve all the anchor tags
    tags = soup('a')
    #print(dir(tags))
    for tag in tags:
       # if tag.__contains__('https') or tag.__contains__('http'):
       print(tag.get('href', None), '\n')


def main():
    # get URL from user
    url = input('Enter URL - ')

    # open given URL, read all contents to the 'html' variable
    html_doc = urllib.request.urlopen(url).read()

    # create BeautifulSoup object
    soup = BeautifulSoup(html_doc, 'html.parser')

    # retrieve all the anchor tags
    tags = soup('a')
    #print(dir(tags))
    for tag in tags:
        if tag.__contains__('https') or tag.__contains__('http'):
           print(tag.get('href', None), '\n')

    # print all anchor tag hyperlinks
    # print_HyperLinks(soup)

if __name__ == '__main__':
    main()