class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     # 暴力解法：双重循环遍历所有可能的两数之和，时间复杂度 O(n^2)
    #     ls = len(nums)
    #     for i in range(ls):
    #         for j in range(i + 1, ls):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    # def twoSum(self, nums, target):
    #     # 哈希表解法 1：先构建完整的哈希表，再遍历查找
    #     hash_nums = {}
    #     # 第一次遍历：将数值作为键，索引列表作为值存入哈希表
    #     for index, num in enumerate(nums):
    #         try:
    #             hash_nums[num].append(index)
    #         except KeyError:
    #             hash_nums[num] = [index]
    #     # 第二次遍历：查找目标差值是否存在于哈希表中
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             candicate = hash_nums[another]
    #             # 如果差值等于当前数，需确保哈希表中该数值对应的索引不止一个（即不是同一个元素）
    #             if another == num:
    #                 if len(candicate) > 1:
    #                     return candicate
    #                 else:
    #                     continue
    #             else:
    #                 return [index, candicate[0]]
    #         except KeyError:
    #             pass

    # def twoSum(self, nums, target):
    #     # 哈希表解法 2：一次遍历，边查找边建表，时间复杂度 O(n)
    #     hash_nums = {}
    #     for index, num in enumerate(nums):
    #         another = target - num
    #         try:
    #             # 尝试查找差值是否已在哈希表中，若存在则直接返回结果
    #             hash_nums[another]
    #             return [hash_nums[another], index]
    #         except KeyError:
    #             # 若不存在，则将当前数值和索引存入哈希表
    #             hash_nums[num] = index

    def twoSum(self, nums, target):
        # 双指针法：先排序再查找，时间复杂度 O(n log n)
        
        # 将数值和原始索引绑定，以便排序后还能找到原始位置
        nums_index = [(v, index) for index, v in enumerate(nums)]
        
        # 对绑定后的列表按数值进行排序
        nums_index.sort()
        
        # 初始化左右指针
        begin, end = 0, len(nums) - 1
        
        while begin < end:
            # 计算当前两个指针指向的数值之和
            curr = nums_index[begin][0] + nums_index[end][0]
            
            if curr == target:
                # 如果和等于目标值，返回对应的原始索引
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                # 如果和小于目标值，左指针右移以增大和
                begin += 1
            else:
                # 如果和大于目标值，右指针左移以减小和
                end -= 1
