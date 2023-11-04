from copy import copy, deepcopy
class Solution:
    def __init__(self):
        self.data = []
    def cp(self) :
        list_1 = [1, 2, [3, 5], 4]## shallow copy
        list_2 = copy(list_1)
        print(list_1[3])
        list_2[3] = 7
        print(list_2[3])
        list_2[2].append(6)
        print(list_1)
        print(list_2)
        ## deep copy   if u dont want orig var to change
        list_3 = deepcopy(list_1)
        list_3[3] = 8
        list_3[2].append(7)
        list_3  # output => [1, 2, [3, 5, 6, 7], 8]
        list_1  # output => [1, 2, [3, 5, 6], 4]


if __name__ == '__main__':
  print('PyCharm')
  s= Solution()
  s.cp()
