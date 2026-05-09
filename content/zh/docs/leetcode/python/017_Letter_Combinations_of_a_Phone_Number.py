# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
dmap = {'2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': ' ',
        None: None}

class Solution(object):
    def letterCombinations(self, digits):
        # 深度优先搜索
        result = []
        ls = len(digits)
        # 空输入返回空列表
        if ls == 0:
            return result
        current = digits[0]
        # 递归获取剩余数字的组合
        posfix = self.letterCombinations(digits[1:])
        # 将当前数字的每个字符与后缀组合拼接
        for t in dmap[current]:
            if len(posfix) > 0:
                for p in posfix:
                    temp = t + p
                    result.append(temp)
            else:
                result.append(t)
        return result


