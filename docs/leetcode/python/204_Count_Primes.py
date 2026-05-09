class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 埃拉托斯特尼筛法
        # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity
        isPrime = [True] * n
        for i in xrange(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                    continue
            # 将i的倍数标记为非质数
            for j in xrange(i * i, n, i):
                isPrime[j] = False
        count = 0
        # 统计质数个数
        for i in xrange(2, n):
            if isPrime[i]:
                count += 1
        return count
