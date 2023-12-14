#Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
import os
from os import listdir
from os.path import isfile, join
class Solution(object):

    def buy(self, prices):
        # prices.sort()
        # print(prices)
        # return prices[len(prices)-1] - prices[0]
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
                right += 1
            return max_profit







if __name__ == '__main__':
    s= Solution()
    print(s.buy([7,1,5,3,6,4]))