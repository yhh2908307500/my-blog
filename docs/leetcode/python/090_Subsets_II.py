class Solution(object):
    # def subsetsWithDup(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res = []
    #     for i in range(1 << len(nums)):
    #         res.append(self.get_subsets(nums, i))
    #     # remove duplicate
    #     final_res = {}
    #     for subset in res:
    #         hash_key = ''.join([str(t) for t in subset])
    #         try:
    #             final_res[hash_key]
    #         except:
    #             final_res[hash_key] = subset
    #     return final_res.values()
    #
    # def get_subsets(self, nums, magic):
    #     res = []
    #     for i in range(len(nums)):
    #         if (1 << i) & magic != 0:
    #             res.append(nums[i])
    #     return res

    def subsetsWithDup(self, nums):
        # 处理重复元素：只在上一次新增的基础上添加
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            if index == 0 or nums[index] != nums[index - 1]:
                # 如果是新元素，从0开始
                begin = 0
            size = len(res)
            # 从begin开始生成新子集
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            # 更新begin，避免重复
            begin = size
        return res
