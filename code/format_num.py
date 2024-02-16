from typing import Optional


class Solution:
    def param_count(*args):
        count_str = "{:,}".format(len(args))  # Convert count to a string with commas as thousands separator
        return count_str


if __name__ == '__main__':
    s=Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(s.param_count("1000000"))

        



        