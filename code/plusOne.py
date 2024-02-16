class Solution:
    def plusOne(self, s: list) -> int:
        my_str = ''.join(map(str, s))
        add = int(my_str) + 1
        return [int(num) for num in str(add)]


if __name__ == '__main__':

   s=Solution()

   print(s.plusOne([1,2,4,9]))

