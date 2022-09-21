import sys
import re

import errno
import os

regexp = r"import \"(.*)\.proto\".*"



def findImports(filename:str):
    occ = []
    try :
        with open(filename) as f:
            for line in f:
                results = re.search(regexp, line.strip())
                if results :
                    occ.append(results.groups()[0])
            return occ
    except FileNotFoundError as e :
        raise e
        

def main():
    '''Get argument values, convert, call findImports.'''
    if len(sys.argv) > 1:
        filename = str(sys.argv[1])
    else:
        filename = str(input('Enter filename: '))

    occ = findImports(filename)

    return occ


if __name__ == "__main__" :
    main()




