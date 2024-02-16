class Solution:
    def __init__(self):
        self.data = []

    def longestCommonPrefix(self, strs) -> str:
        v = sorted(strs)
        ans = ""
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans









if __name__ == '__main__':
  print('PyCharm')
  s= Solution()

  print(s.longestCommonPrefix(["flower","flow","flight","world"]))