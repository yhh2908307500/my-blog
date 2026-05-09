import itertools as it
 class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 使用itertools生成所有k个数的组合，筛选和为n的组合
        return list(it.ifilter(lambda x: sum(x) == n, list(it.combinations(range(1, 10), k))))
