class TwoSum(object):

    def __init__(self):
        """
        初始化数据结构
        """
        self.internal = []
        self.dic = {}

    def add(self, number):
        """
        将数字添加到内部数据结构
        :rtype: nothing
        """
        self.internal.append(number)
        if number in self.dic:
            # 数字已存在，标记为出现多次
            self.dic[number] = True
            return
        # 数字首次出现
        self.dic[number] = False

    def find(self, value):
        """
        查找是否存在一对数字之和等于value
        :type value: int
        :rtype: bool
        """
        for v in self.internal:
            if value - v in self.dic:
                # 如果需要两个相同的数字，但该数字只出现一次，则跳过
                if v << 1 == value and not self.dic[v]:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
