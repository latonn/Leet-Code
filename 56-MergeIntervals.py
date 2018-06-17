#

# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # latonn's
        result = []
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals)):
            if i == 0:
                result.append(intervals[0])
            else:
                if result[-1].start <= intervals[i].start <= result[-1].end:
                    result[-1].end = max(intervals[i].end, result[-1].end)
                else:
                    result.append(intervals[i])

        # for k in result:
        #     print(k.start, k.end)
        return result


if __name__ == '__main__':
    a = Interval(1, 4)
    b = Interval(0, 5)
    # c = Interval(8, 10)
    # d = Interval(15, 18)
    intervals = [a, b]
    print(Solution().merge(intervals))
