# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from itertools import groupby

# since its sequential use stack

def cleanstring(s, k):
    stack=[]
    for i in s:
        if stack and stack[-1][0]==i:
            stack[-1][1]+=1
        else:
            stack.append([i,1])
        if stack and stack[-1][1]==k:
            stack.pop()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    repeatedly make k duplicate removals on s until we no longer can.
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation: 
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"
     '''
    s = 'pbbcggttciiippooaais'

    k = 2

    cleans = cleanstring(s, k)
    print(cleans)

