class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        half = []
        res = []
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        odd, even = 0, 0
        for c in dic:
            if dic[c] % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd > 1:
            return []
        # 生成一半的字符，然后排列组合
        seed = []
        mid = ''
        for c in dic:
            if dic[c] % 2 == 1:
                mid = c
            seed.extend([c] * (dic[c] / 2))
        self.permute(half, seed, 0)
        # 合并成完整的回文
        for r in half:
            res.append(''.join(r) + mid + ''.join(reversed(r)))
        return res

    def permute(self, res, num, index):
        # 回溯法生成排列，去重
        if index == len(num):
            res.append(list(num))
            return
        appeared = set()
        for i in range(index, len(num)):
            if num[i] in appeared:
                continue
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            self.permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]
