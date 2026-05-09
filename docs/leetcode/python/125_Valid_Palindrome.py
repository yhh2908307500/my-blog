class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 只保留字母数字并转小写，双指针检查
        alnum_s = [t.lower() for t in s if t.isalnum()]
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls / 2
        for i in range(mid):
            if alnum_s[i] != alnum_s[ls - 1 - i]:
                return False
        return True