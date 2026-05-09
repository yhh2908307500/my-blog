class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        # 过滤空字符串
        temp = [t for t in temp if len(t) > 0]
        if len(temp) == 0:
            return 0
        else:
            return len(temp[-1])