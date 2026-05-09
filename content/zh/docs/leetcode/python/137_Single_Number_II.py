class Solution(object):
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     import ctypes
    #     # note that if res is not c 32
    #     # there will be errors
    #     count = [0] * 32
    #     res = ctypes.c_int32(0)
    #     for i in range(32):
    #         for num in nums:
    #             if (ctypes.c_int32(num).value >> i) & 1:
    #                 count[i] += 1
    #         res.value |= ((count[i] % 3) << i)
    #     return res.value

    def singleNumber(self, nums):
        # 位掩码：ones记录出现一次，twos记录出现两次，threes记录出现三次
        # 当某数位出现三次时，在ones和twos中清除
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones