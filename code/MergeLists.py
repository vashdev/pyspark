from typing import Optional


class Solution:
    def mergeTwoLists(self, list1,list2) -> []:
        return [[x, y] for x in list1 for y in list2 if 1 == 1]
    



if __name__ == '__main__':
    s=Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(s.mergeTwoLists(list1,list2))

        



        