#Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
import os
from os import listdir
from os.path import isfile, join
from queue import LifoQueue

class Solution(object):
    def removeVowels(self, s: str) -> str:
        return ''.join( c for c in s if  c not in 'aeiou' )

if __name__ == '__main__':
    s= Solution()
    print(s.removeVowels("hello"))