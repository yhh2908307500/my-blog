# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
class Solution(object):
    def generateParenthesis(self, n):
        # 递归：在n-1的结果基础上插入新的括号
        if n == 1:
            return ['()']
        last_list = self.generateParenthesis(n - 1)
        res = []
        for t in last_list:
            curr = t + ')'
            # 在每个右括号前插入左括号
            for index in range(len(curr)):
                if curr[index] == ')':
                    res.append(curr[:index] + '(' + curr[index:])
        # 去重后返回
        return list(set(res))


    # def generateParenthesis(self, n):
    #     def generate(leftnum, rightnum, s, result):
    #         if leftnum == 0 and rightnum == 0:
    #             result.append(s)
    #         if leftnum > 0:
    #             generate(leftnum - 1, rightnum, s + '(', result)
    #         if rightnum > 0 and leftnum < rightnum:
    #             generate(leftnum, rightnum - 1, s + ')', result)
    #
    #     result = []
    #     s = ''
    #     generate(n, n, s, result)
    #     return result
