#Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
import os
from os import listdir
from os.path import isfile, join
from queue import LifoQueue

class Solution(object):
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        n = len(s)
        left = 0
        right = n - 1
        vowels = set('AEIOUaeiou')
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        s = ''.join(s)
        return s
if __name__ == '__main__':
    s= Solution()
    print(s.reverseVowels("hello"))