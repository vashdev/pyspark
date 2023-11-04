# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from functools import reduce
from itertools import groupby, accumulate

def l(s):
    uniqChars=''
    maxfound=''
    lastchar=''
    for index, letter in enumerate(s):
        print(index,letter)
        print(f"{index} let={letter}   lastchar= {lastchar}  uniqchar= f{uniqChars}")
        if index ==0:
            uniqChars=letter
            lastchar=letter

        elif letter  == lastchar:
                 maxfound=uniqChars
                 uniqChars=''
        else:
            uniqChars=uniqChars+letter
            lastchar=letter
    return uniqChars








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(l("abcabcbb"))