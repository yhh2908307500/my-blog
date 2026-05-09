class Solution:
    def maximum69Number (self, num: int) -> int:
        # 将第一个6替换成9
        return(str(num).replace('6', '9', 1))
