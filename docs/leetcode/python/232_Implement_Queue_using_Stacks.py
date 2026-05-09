# class Queue(object):
#     def __init__(self):
#         """
#         初始化数据结构
#         """
#         self.stack1 = []
#         self.stack2 = []
#
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         # 每次push时将stack1的元素移到stack2，加入新元素，再移回stack1
#         while len(self.stack1) > 0:
#             curr = self.stack1.pop()
#             self.stack2.append(curr)
#         self.stack1.append(x)
#         while len(self.stack2) > 0:
#             curr = self.stack2.pop()
#             self.stack1.append(curr)
#
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.stack1.pop()
#
#
#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.stack1[-1]
#
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.stack1) == 0

class Queue(object):
    def __init__(self):
        """
        初始化数据结构
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # 新元素加入stack1
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        # stack2为空时将stack1的元素移到stack2
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        self.stack2.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1):
                curr = self.stack1.pop()
                self.stack2.append(curr)
        return self.stack2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack1) + len(self.stack2) == 0