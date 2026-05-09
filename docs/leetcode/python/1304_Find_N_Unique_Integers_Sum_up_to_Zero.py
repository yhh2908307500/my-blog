class Solution:
    def sumZero(self, n: int) -> List[int]:
        # 1到n-1，再加上它们的和的相反数
        prefix_sum = 0
        res = []
        for i in range(1, n):
            res.append(i)
            prefix_sum = prefix_sum + i
        res.append(-prefix_sum)
        return res
    
    # def sumZero(self, n: int) -> List[int]:
    #     # 1,n-1
    #     prefix = list(range(1, n))
    #     # sum(from 1 to n-1)
    #     return prefix + [-sum(prefix)]
