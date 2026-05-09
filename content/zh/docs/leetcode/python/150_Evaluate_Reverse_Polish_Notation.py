class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 用栈计算逆波兰表达式：遇到数字入栈，遇到运算符弹出两个数计算
        stack = []
        for t in tokens:
            try:
                temp = int(t)
                stack.append(temp)
            except:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    a += b
                elif t == "-":
                    a -= b
                elif t == "*":
                    a *= b
                else:
                    a = int(a * 1.0 / b)
                stack.append(a)
        return stack[-1]