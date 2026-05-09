class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # 先从高位匹配num1的1，剩余1从低位填充，使异或结果最小
        num1, num2 = bin(num1)[2:], bin(num2)[2:]
        lenNum1, lenNum2 = len(num1), len(num2)
        ones = num2.count("1")
        maxLen = max(lenNum1, lenNum2)

        ans = []
        for _ in range(maxLen):
            ans.append("0")

        for _ in range(maxLen - lenNum1):
            num1 = "0" + num1

        for _ in range(maxLen - lenNum2):
            num2 = "0" + num2

        for i in range(len(num1)):
            if num1[i] == "1" and ones:
                ans[i] = "1"
                ones -= 1

        for i in range(len(ans) - 1, -1, -1):
            if ones < 1:
                break

            if ans[i] == "1":
                continue

            ans[i] = "1"
            ones -= 1

        ans = "".join(ans)
        return int(ans, 2)
