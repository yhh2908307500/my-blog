class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 单调栈：保持递增顺序
        largest_rectangle = 0
        ls = len(heights)
        stack = [-1]
        top, pos = 0, 0
        for pos in range(ls):
            # 当遇到更小的元素时，计算栈顶元素的面积
            while top > 0 and heights[stack[top]] > heights[pos]:
                largest_rectangle = max(largest_rectangle, heights[stack[top]] * (pos - stack[top - 1] - 1))
                top -= 1
                stack.pop()
            stack.append(pos)
            top += 1
        # 处理栈中剩余元素
        while top > 0:
            largest_rectangle = max(largest_rectangle, heights[stack[top]] * (ls - stack[top - 1] - 1))
            top -= 1
        return largest_rectangle


if __name__ == "__main__":
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
