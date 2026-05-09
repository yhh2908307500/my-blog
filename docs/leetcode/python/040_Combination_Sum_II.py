class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 动态规划，存储索引避免重复使用
        candidates.sort()
        dp = [[] for _ in range(target + 1)]
        dp[0].append([])
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                for k in range(len(dp[i - candidates[j]])):
                    temp = dp[i - candidates[j]][k][:]
                    # 检查该数字是否已使用
                    if len(temp) > 0 and temp[-1] >= j:
                        continue
                    # 存储索引
                    temp.append(j)
                    dp[i].append(temp)
        res = []
        check = {}
        for temp in dp[target]:
            value = [candidates[t] for t in temp]
            try:
                check[str(value)] += 1
            except KeyError:
                check[str(value)] = 1
                res.append(value)
        return res