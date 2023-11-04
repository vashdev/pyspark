class Solution:
    def countLetters(self, s: str) -> int:
            total = 1
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    count = 1
                total += count
            return total


if __name__ == '__main__':
    print(' ')
    s=Solution()
    print(s.countLetters('aaaaaaaaaa'))

        



        