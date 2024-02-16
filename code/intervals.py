# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from itertools import groupby


def merge(intervals: list[list[int]]) -> list[list[int]]:
    ans=[]
    intervals.sort()
    start=intervals[0][0]
    end=intervals[0][1]
    for n in range(1,len(intervals)):
        print(intervals[n],n, len(intervals))
        if intervals[n][0] < end < intervals[n][1]:
            end = intervals[n][1]
        else:
            ans.append([start, end])
            start=intervals[n][0]
            end=intervals[n][1]
    ans.append([start, end])
    return ans

# Press the green button in  to run the script.
if __name__ == '__main__':
    '''
    Given an array of intervals where intervals[i] = [starti, endi], 
    merge all overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.
    '''
    print(merge([[1,3],[2,6],[8,10],[15,18]]))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
