# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from itertools import groupby, accumulate


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self, l1: ListNode, l2: ListNode):
        self.l1 = l1
        self.l2 = l2
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        string1 = ""
        while l1 != None:
            string1 = str(l1.val) + string1
            l1 = l1.next
        string2 = ""
        while l2 != None:
            string2 = str(l2.val) + string2
            l2 = l2.next
        num = int(string1) + int(string2)
        dummy = ListNode(0)
        first = dummy
        for digit in str(num)[::-1]:
            first.next = ListNode(int(digit))
            first = first.next
        return dummy.next

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(' ')
    l1 = ListNode([2, 4, 3]);
    l2 = ListNode([5, 6, 4]);
    l3=Solution(l1,l2)
    l4=l3.addTwoNumbers(l1,l2)
    print(l4)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
