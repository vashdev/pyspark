class Solution:
    def __init__(self):
        self.data = []
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x % 10
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        v = sorted(strs)
        print(v[0], "-1", v[-1], min(len(v[0]), len(v[-1])))

        for i in range(min(len(v[0]), len(v[-1]))):
            if v[0][i] != v[-1][i]:
                return res
            res += v[0][i]
        return res








if __name__ == '__main__':
  print('PyCharm')
  s= Solution()
  y = s.isPalindrome(121)
  if 121 == y:
   print(" True ")
  print(s.longestCommonPrefix(["flower","flow","flight","world"]))