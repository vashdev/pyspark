
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
def isPalindrome(x):
     if str(x) == str(x)[::-1]:
         return True
     else:
         False


if __name__ == '__main__':
    print(isPalindrome("121"))