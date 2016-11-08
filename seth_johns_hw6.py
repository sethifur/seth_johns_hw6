#!/usr/bin/env python3
import sys
import urllib.request
import re
import pprint
import heapq


def helpUsage():
    """
    Prints how the program is to be used
    """
    print('Usage is: ./seth_johns_hw6.py <file input>')


def readFile(url):
    """
    readFile reads an error file and prints the top 25 errors
    Args:
        url address to a error log
    """
    webText = urllib.request.urlopen(url)
    text = webText.read()
    pattern = '\/([0-9a-zA-Z\.]*)*'
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
    getMax(dictResult)
    #for index in dictResult:        
    #    print(index,'\t',dictResult[index],'\n')
    

def getMax(begin):
    """
    prints out the top 25 errors
    Args:
        begin is a dictionary with the list of errors and how many times that error re occurs
    """
    results = heapq.nlargest(25,begin,key=begin.get)
    print('*** Top 25 page errors ***')
    for i in results:
        print('Count:',begin[i],'\t','page: ',i,'\n')

# Main Function
def main():
    """
    Tests readFile
    """
    #url = 'http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test'

    try:
        url = sys.argv[1]
        readFile(url)
    except IndexError:
        helpUsage()
    
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
