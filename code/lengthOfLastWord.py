class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: x.strip(), s.split(" ") ))[-1])


if __name__ == '__main__':

   s=Solution()

   print(s.lengthOfLastWord("hello world "))

