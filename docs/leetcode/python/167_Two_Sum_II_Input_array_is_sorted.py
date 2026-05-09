class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 双指针：数组有序，左指针从左，右指针从右
        begin, end = 0, len(numbers) - 1
        while begin < end:
            curr = numbers[begin] + numbers[end]
            if curr == target:
                return [begin + 1, end + 1]
            elif curr < target:
                begin += 1
            else:
                end -= 1

