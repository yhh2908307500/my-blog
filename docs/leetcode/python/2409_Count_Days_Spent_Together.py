class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # 将日期转换为一年中的第几天，用数组标记重叠日期
        arriveAliceMonth, arriveAliceDay = map(int, arriveAlice.split("-"))
        leaveAliceMonth, leaveAliceDay = map(int, leaveAlice.split("-"))
        arriveBobMonth, arriveBobDay = map(int, arriveBob.split("-"))
        leaveBobMonth, leaveBobDay = map(int, leaveBob.split("-"))

        calendar = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefixOfCalendar = [0] * 13
        totalDates = sum(calendar)
        spentTogether, aliceSpent = [0] * (totalDates + 1), [0] * (totalDates + 1)

        for i in range(1, len(calendar)):
            prefixOfCalendar[i] = prefixOfCalendar[i - 1] + calendar[i]

        arriveAliceTotal = prefixOfCalendar[arriveAliceMonth - 1] + arriveAliceDay
        leaveAliceTotal = prefixOfCalendar[leaveAliceMonth - 1] + leaveAliceDay
        for i in range(arriveAliceTotal, leaveAliceTotal + 1):
            aliceSpent[i] += 1

        arriveBobTotal = prefixOfCalendar[arriveBobMonth - 1] + arriveBobDay
        leaveBobTotal = prefixOfCalendar[leaveBobMonth - 1] + leaveBobDay
        for i in range(arriveBobTotal, leaveBobTotal + 1):
            if aliceSpent[i]:
                spentTogether[i] += 1

        return sum(spentTogether)
