#!/usr/bin/env python3
import sys
import urllib.request
import re
import pprint
import heapq


def readFile(url):
    webText = urllib.request.urlopen(url)
    text = webText.read()
    pattern = '\/[0-9a-zA-Z]*\/[0-9a-zA-Z]*\/[0-9a-zA-Z]*\/[0-9a-zA-Z]*'
    text = text.replace(b'\n',b' ')
    text = text.replace(b',' , b'')
    bitStringArray = text.split()
    stringArray = []
    for index in bitStringArray:
        stringArray.append(index.decode('utf-8'))
    narrowSearch = []
    for index in stringArray:
        if re.match(pattern, index):
            narrowSearch.append(index)
    dictResult = dict()
    for index in narrowSearch:
        if dictResult.get(index) == None:
            dictResult[index] = 1
        else: 
            dictResult[index] += 1
    minMax(dictResult)
    #for index in dictResult:        
    #    print(index,'\t',dictResult[index],'\n')
    

def minMax(begin):
    results = heapq.nlargest(25,begin,key=begin.get)
    for i in results:
        print(i,'\t',begin[i],'\n')

# Main Function
def main():
    """
    Tests readFile
    """
    #url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test'
    url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full'
    readFile(url)
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
