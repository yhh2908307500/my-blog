# class Solution(object):
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
class Solution(object):
    def threeSumClosest(self, nums, target):
        ls = len(nums)
        # 先排序数组
        sort_nums = sorted(nums)
        # 初始化结果为前三个数的和
        res = nums[0] + nums[1] + nums[2]
        # 固定第一个数
        for i in range(ls - 2):
            j, k = i + 1, ls - 1
            # 双指针查找另外两个数
            while j < k:
                temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
                # 如果当前和更接近目标，更新结果
                if abs(target - temp) < abs(target - res):
                    res = temp
                if temp < target:
                    # 和太小，左指针右移
                    j += 1
                else:
                    # 和太大，右指针左移
                    k -= 1
        return res


