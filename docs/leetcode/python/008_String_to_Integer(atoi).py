class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 符号标记，默认为正
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        result, pos = 0, 0
        ls = len(str)
        # 跳过开头的空格
        while pos < ls and str[pos] == ' ':
            pos += 1
        # 处理符号
        if pos < ls and str[pos] == '-':
            sign = -1
            pos += 1
        elif pos < ls and str[pos] == '+':
            pos += 1
        # 处理数字
        while pos < ls and ord(str[pos]) >= ord('0') and ord(str[pos]) <= ord('9'):
            num = ord(str[pos]) - ord('0')
            # 检查溢出
            if result > max_int / 10 or ( result == max_int / 10 and num >= 8):
                if sign == -1:
                    return min_int
                return max_int
            result = result * 10 + num
            pos += 1
        return sign * result

    # def myAtoi(self, s):
    #     #https://leetcode.com/discuss/83626/line-python-solution-eafp-instead-lbyl-easier-logic-beats-24%25
    #     try:
    #         s = s.lstrip() + '$' # remove leading spaces and append an end mark
    #         for i, ch in enumerate(s):
    #             if not (ch in '+-' or '0' <= ch <= '9'):
    #                 result = int(s[:i])
    #                 return -2 ** 31 if result < -2 ** 31 else 2 ** 31 - 1 if result > 2 ** 31 - 1 else result
    #     except:
    #         return 0


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.myAtoi("+-2")