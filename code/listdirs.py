#Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
import os
from os import listdir
from os.path import isfile, join
class Solution(object):

    def filelist(self, mypath):
        return [os.path.join(r,file) for r,d,f in os.walk(mypath) for file in f]


if __name__ == '__main__':
    s= Solution()
    print(s.filelist('/Users/akula/src/'))