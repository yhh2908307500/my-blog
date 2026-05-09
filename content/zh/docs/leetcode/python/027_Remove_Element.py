# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
class Solution(object):
    # def removeElement(self, nums, val):
    #     ls = len(nums)
    #     if ls == 0:
    #         return ls
    #     pos = 0
    #     for i in range(ls):
    #         if nums[i] == val:
    #             continue
    #         else:
    #             nums[pos] = nums[i]
    #             pos += 1
    #     # del nums[pos:]
    #     return pos

    def removeElement(self, nums, val):
        # 从末尾交换元素，避免多次移动
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:
            if nums[index] == val:
                # 用末尾元素替换
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
        return ls - count

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.removeElement([1], 1)

