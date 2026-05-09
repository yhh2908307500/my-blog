class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ls = len(s)
        word_ls = len(words[0])
        target_dict = {}
        # 统计每个单词出现次数
        for word in words:
            try:
                target_dict[word] += 1
            except KeyError:
                target_dict[word] = 1
        res = []
        # 遍历所有可能的起始位置
        for start in range(ls - word_ls * len(words) + 1):
            curr_dict = target_dict.copy()
            # 检查每个单词是否匹配
            for pos in range(start, start + word_ls * len(words), word_ls):
                curr = s[pos:pos + word_ls]
                try:
                    curr_dict[curr] -= 1
                    # 单词出现次数超过目标
                    if curr_dict[curr] < 0:
                        break
                except KeyError:
                    # 单词不在目标中
                    break
            else:
                # 所有单词都匹配
                res.append(start)
        return res

    # def findSubstring(self, s, words):
    #     # https://leetcode.com/discuss/87745/3-line-python-solution-sorted-hash-112ms
    #     wLen, wtLen, wSet, sortHash, sLen = len(words[0]), len(words[0]) * len(words), set(words), sorted(
    #         [hash(w) for w in words]), len(s)
    #     h = [hash(s[i:i + wLen]) if s[i:i + wLen] in wSet else None for i in xrange(sLen - wLen + 1)]
    #     return [i for i in xrange(sLen - wtLen + 1) if h[i] and sorted(h[i: i + wtLen: wLen]) == sortHash]

if __name__ == '__main__':
    s = Solution()
    # print s.longestValidParentheses(")(((((()())()()))()(()))(")
    print s.findSubstring('wordgoodgoodgoodbestword', ["word", "good", "best", "good"])

    # [6,9,12]




