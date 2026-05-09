class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        ls, pos = len(s), 0
        if s is None or ls == 0:
            return
        # 先整体反转
        self.reverse(s, 0, ls)
        # 再逐个单词反转
        for i in range(ls + 1):
            if i == ls or s[i] == ' ':
                self.reverse(s, pos, i)
                pos = i + 1

    def reverse(self, array_s, begin, end):
        # 双指针反转数组片段
        for i in range((end - begin) / 2):
            array_s[begin + i], array_s[end - i - 1] = array_s[end - i - 1], array_s[begin + i]
