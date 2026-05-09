class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 使用反转单词字典，检查前缀和后缀
        word2index, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, word in enumerate(words):
            for j in xrange(len(word) + 1):
                prefix, postfix = word[:j], word[j:]
                # 前缀 + 后缀 + 反转前缀
                if prefix in word2index and i != word2index[prefix] and postfix == postfix[::-1]:
                    res.append([i, word2index[prefix]])
                # 反转后缀 + 前缀 + 后缀
                if j > 0 and postfix in word2index and i != word2index[postfix] and prefix == prefix[::-1]:
                    res.append([word2index[postfix], i])
        return res
