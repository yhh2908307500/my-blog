class Solution:
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     roman = {'I': 1, 'V': 5, 'X': 10,
    #              'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     result = 0
    #     last = s[-1]
    #     for t in reversed(s):
    #         if t == 'C' and last in ['D', 'M']:
    #             result -= roman[t]
    #         elif t == 'X' and last in ['L', 'C']:
    #             result -= roman[t]
    #         elif t == 'I' and last in ['V', 'X']:
    #             result -= roman[t]
    #         else:
    #             result += roman[t]
    #         last = t
    #     return result

    def romanToInt(self, s):
        # 罗马字符到整数的映射
        roman = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev, total = 0, 0
        for c in s:
            curr = roman[c]
            total += curr
            # 如果当前字符值大于前一个，说明是特殊情况如IV、IX等，需要减去2倍的前一个值
            if curr > prev:
                total -= 2 * prev
            prev = curr
        return total

