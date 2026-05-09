# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    # def canAttendMeetings(self, intervals):
    #     """
    #     :type intervals: List[Interval]
    #     :rtype: bool
    #     """
    #     # 如果是开始时间则count += 1
    #     # 如果是结束时间则count -= 1
    #     # 如果count >= 2，则返回False
    #     check = []
    #     for it in intervals:
    #         check.append((it.start, True))
    #         check.append((it.end - 1, False))
    #     check.sort(key=lambda x : x[0])
    #     count = 0
    #     for t in check:
    #         if t[1]:
    #             count += 1
    #             if count > 1:
    #                 return False
    #         else:
    #             count -= 1
    #     return True

    def canAttendMeetings(self, intervals):
        # 按开始时间排序，检查相邻会议是否重叠
        intervals.sort(key=lambda x: x.start)
        ls = len(intervals)
        for i in range(ls - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True
