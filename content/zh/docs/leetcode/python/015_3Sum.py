
class Solution(object):
    # def threeSum(self, nums):
    #     # skip duplicate
    #     # O(n^3)
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     ls = len(nums)
    #     result = []
    #     for i in range(0, ls - 2):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         j = i + 1
    #         k = ls - 1
    #         while(j < k):
    #             temp = [nums[i], nums[j], nums[k]]
    #             s = sum(temp)
    #             jtemp = nums[j]
    #             ktemp = nums[k]
    #             if s <= 0:
    #                 j += 1
    #                 while(j < k and jtemp == nums[j]):
    #                     j += 1
    #                 if s == 0:
    #                     result.append(temp)
    #             else:
    #                 k -= 1
    #                 while(j < k and ktemp == nums[k]):
    #                     k -= 1
    #     return result
    # def threeSum(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #     """
    #     # using multiple 2 sum
    #     nums.sort()
    #     result, visited = set(), {}
    #     for i in xrange(len(nums) - 2):
    #         table, target = {}, -nums[i]
    #         if nums[i] not in visited:
    #             for j in xrange(i + 1, len(nums)):
    #                 if nums[j] not in table:
    #                     table[target - nums[j]] = j
    #                 else:
    #                     result.add((nums[i], target - nums[j], nums[j]))
    #             visited[nums[i]] = 1
    #     return list(result)

    def threeSum(self, nums):
        res = []
        # 先排序数组
        nums.sort()
        ls = len(nums)
        # 固定第一个数
        for i in range(ls - 2):
            # 跳过重复的第一个数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            # 双指针查找另外两个数
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # 跳过重复的第二个数
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # 跳过重复的第三个数
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr < 0:
                    # 和太小，左指针右移
                    j += 1
                else:
                    # 和太大，右指针左移
                    k -= 1
        return res
