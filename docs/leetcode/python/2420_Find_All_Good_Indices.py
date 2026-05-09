#2420_Find_All_Good_Indices.py
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # 前缀和统计递增递减次数，检查前后k个区间是否满足条件
        posi, nega = [0], [0]

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            posi.append(posi[i - 1])
            nega.append(nega[i - 1])

            if diff > 0:
                posi[i] += 1
            elif diff < 0:
                nega[i] += 1

        ans = []
        for i in range(k, len(nums) - k):
            if i + k >= len(nums):
                break

            if nega[i + k] - nega[i + 1] > 0:
                continue
            if posi[i - 1] - posi[i - k] > 0:
                continue

            ans.append(i)
        return ans