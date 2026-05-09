class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心：只要后一天比前一天高，就累加
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])
