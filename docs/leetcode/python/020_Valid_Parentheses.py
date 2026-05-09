# class Solution(object):
#     def isValid(self, s):
        
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        # 使用栈来处理括号匹配
        stack = []
        for t in s:
            if t == ')':
                try:
                    current = stack.pop()
                    if current != '(':
                        return False
                except:
                    return False
            elif t == '}':
                try:
                    current = stack.pop()
                    if current != '{':
                        return False
                except:
                    return False
            elif t == ']':
                try:
                    current = stack.pop()
                    if current != '[':
                        return False
                except:
                    return False
            else:
                # 左括号入栈
                stack.append(t)
        # 栈为空表示所有括号都匹配
        if len(stack) == 0:
            return True
        else:
            return False


    # def isValid(self, s):
    #     # python replace
    #     n = len(s)
    #     if n == 0:
    #         return True
    #
    #     if n % 2 != 0:
    #         return False
    #
    #     while '()' in s or '{}' in s or '[]' in s:
    #         s = s.replace('{}', '').replace('()', '').replace('[]', '')
    #
    #     if s == '':
    #         return True
    #     else:
    #         return False
