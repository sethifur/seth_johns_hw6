#!/usr/bin/env python3
import sys
import urllib.request

def readFile(url):
    webText = urllib.request.urlopen(url)
    text = webText.read()
    print(text)

# Main Function
def main():
    """
    Tests readFile
    """
    url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test'
    #url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full'
    readFile(url)
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
