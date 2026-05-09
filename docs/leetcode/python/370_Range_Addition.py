class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # 差分数组：记录区间起始和结束位置，最后累加
        res = [0] * length
        for t in updates:
            start, end, val = t
            res[start] += val
            if end < length - 1:
                res[end + 1] -= val
        for i in range(1, length):
            res[i] = res[i] + res[i - 1]
        return res
