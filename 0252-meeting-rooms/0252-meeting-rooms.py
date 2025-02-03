class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals) - 1):
            a, b = intervals[i]
            for j in range(i + 1, len(intervals)):
                c, d = intervals[j]
                if c < b and c >= a:
                    return False
                if a < d and a >= c:
                    return False
        return True