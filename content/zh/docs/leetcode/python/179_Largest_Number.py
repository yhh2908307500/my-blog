class LargerNumKey(str):
    def __lt__(x, y):
        # 自定义比较规则：比较x+y和y+x的大小
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        # 将数字转为字符串，按自定义规则排序后拼接
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        # 处理前导0的情况
        return '0' if largest_num[0] == '0' else largest_num
