class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def longestConsecutive(self, num):
            # 用集合找连续序列，左右延伸，O(n)时间空间
            num = set(num)
            maxLen = 0
            while num:
                n = num.pop()
                i = n + 1
                l1 = 0
                l2 = 0
                while i in num:
                    num.remove(i)
                    i += 1
                    l1 += 1
                i = n - 1
                while i in num:
                    num.remove(i)
                    i -= 1
                    l2 += 1
                maxLen = max(maxLen, l1 + l2 + 1)
            return maxLen