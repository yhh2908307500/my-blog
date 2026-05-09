class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 统计字符出现次数，回文排列要求奇数次数的字符不超过1个
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        for c in dic:
            if dic[c] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd <= 1:
            return True
        return False
