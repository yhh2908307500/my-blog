class Solution:
    # def myPow(self, x, n):
    #     """
    #     :type x: float
    #     :type n: int
    #     :rtype: float
    #     """
    #     if n == 0:
    #         return 1
    #     temp = pow(x, n / 2)
    #     if n % 2 == 0:
    #         return temp * temp
    #     else:
    #         return temp * temp * x

    def myPow(self, x, n):
        # https://leetcode.com/discuss/93413/iterative-log-n-solution-with-clear-explanation
        # 9 = 2^3 + 2^0 = 1001
        # x^9 = x^(2^3)*x(2^0)
        # 当二进制位为1时乘以x^i
        if n == 0:
            return 1
        res ,curr = 1, abs(n)
        while curr > 0:
            if curr & 1 == 1:
                res *= x
            curr >>= 1
            x *= x
        if n < 0:
            return 1 / res
        return  res
