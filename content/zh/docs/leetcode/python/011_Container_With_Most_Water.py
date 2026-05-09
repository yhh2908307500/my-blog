class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针法
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            # 计算当前面积：高度取左右指针中的较小值，宽度是两指针间距
            result = max(min(height[left], height[right]) * (right - left), result)
            # 移动较矮的指针，因为移动较高的指针无法增加面积
            if height[left] > height[right]:
                # 移除右指针
                right -= 1
            else:
                # 移除左指针
                left += 1
        return result
