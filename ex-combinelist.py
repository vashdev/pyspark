class Solution:
    def __init__(self):
        self.data = []
    def comblist(self) -> bool:
        a = [1, 2, 3]
        b = [7, 8, 9]
        f = a + b
        print(f)
        c=[(x + y) for (x, y) in zip(a, b)]  # parallel iterators
        print(c)
        # output => [8, 10, 12]
        d=[(x, y) for x in a for y in b]  # nested iterators
        # output => [(1, 7), (1, 8), (1, 9), (2, 7), (2, 8), (2, 9), (3, 7), (3, 8), (3, 9)]
        print(d)
        my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        flattened = [x for temp in my_list for x in temp]
        print(flattened)


if __name__ == '__main__':
  print('PyCharm')
  s= Solution()
  y = s.comblist()
