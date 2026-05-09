class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        """
            n : positive integer
            return : smallest positive integer that is a multiple of both 2 and n
        """
        # 偶数返回本身，奇数返回n*2
        if n % 2 == 0:
            return n
        
        return n * 2
        
