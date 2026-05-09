from collections import OrderedDict
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # https://discuss.leetcode.com/topic/19991/o-n-python-using-buckets-with-explanation-10-lines
        # 桶排序。每个桶大小为t。对于每个数字，可能的候选只能在同一个桶或相邻的两个桶中。
        # 最多保持k个桶以确保索引差不超过k。
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0是特殊情况，只需要检查v所在的桶
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # 移除太远的桶。注意t为0的情况
                del buckets[nums[i - k] / t if t else nums[i - k]]

        return False
