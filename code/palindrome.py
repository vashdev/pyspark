class Solution:
    def __init__(self):
        self.data = []
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return  str(x) == str(x)[::-1]
    def ispalindromRec(selfself,num:int) ->bool:
        temp = num
        rev = 0
        while (num > 0):
            dig = num % 10
            rev = rev * 10 + dig
            num = num // 10
        if (temp == rev):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!")




if __name__ == '__main__':
  print('PyCharm')
  s= Solution()
  s.isPalindrome(121)
  print(s.longestCommonPrefix(["flower","flow","flight","world"]))