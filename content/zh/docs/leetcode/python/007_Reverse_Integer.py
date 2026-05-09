class Solution:
    def reverse(self, x):
        # https://leetcode.com/problems/reverse-integer/
#        flag = True if x < 0 else False
#       if flag:
#           x = -x
#       x = str(x)[::-1]

#       if flag:
#           x = "-" + x

#       value = 2 ** 31
#       x = int(x)
#       if -value <= x < value:
#           return x
#       return 0
        
        # 标记是否为负数
        is_neg = False
        if x < 0:
            x = -x
            is_neg = True

        # 反转数字
        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x //= 10
        # 恢复符号
        if is_neg:
            res = -res

        # 检查是否溢出32位有符号整数范围
        if res < -2**31 or res > 2**31-1:
            return 0
        return res
    