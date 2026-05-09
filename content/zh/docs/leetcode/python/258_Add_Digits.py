class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https: // en.wikipedia.org / wiki / Digital_root
        # 数字根公式
        if num < 10:
            return num
        return num - ((num - 1) / 9) * 9