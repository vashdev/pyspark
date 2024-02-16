from copy import copy, deepcopy
class Solution:
    def __init__(self):
        self.data = []
    def cp(self) :
        list_1 = [1, 2, [3, 5], 4]## shallow copy
        list_2 = copy(list_1) #copy or deep copy  creates new object not just another ref
        l2=list_1

        list_1[0]=0
        print(list_1, "copy uneffected", list_2, " reference is effected",l2)




if __name__ == '__main__':
  print('PyCharm')
  s= Solution()
  s.cp()
