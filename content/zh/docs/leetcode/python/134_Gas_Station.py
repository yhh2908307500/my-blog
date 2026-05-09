class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # 双指针：如果当前剩余油量大于0，从begin出发；否则从end出发
        ls = len(gas)
        begin, end = 0, ls - 1
        curr = gas[end] - cost[end]
        while begin < end:
            if curr >= 0:
                curr += gas[begin] - cost[begin]
                begin += 1
            else:
                end -= 1
                curr += gas[end] - cost[end]
        if curr >= 0:
            return end
        else:
            return -1

