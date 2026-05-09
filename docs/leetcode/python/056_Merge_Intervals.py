# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None:
            return
        ls = len(intervals)
        if ls <= 1:
            return intervals
        # 按起始位置排序
        intervals.sort(key=lambda x: x.start)
        pos = 0
        while pos < len(intervals) - 1:
            # 检查重叠
            if intervals[pos].end >= intervals[pos + 1].start:
                next = intervals.pop(pos + 1)
                # 检查下一个是重叠还是完全被当前覆盖
                if next.end > intervals[pos].end:
                    intervals[pos].end = next.end
                # print [(t.start, t.end) for t in intervals], pos
            else:
                pos += 1
        return intervals

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.merge([[1,3],[2,6],[8,10],[15,18]])