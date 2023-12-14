#Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()



if __name__ == '__main__':
    s= Solution()
    print(s.singleNumber([2,2,1]))