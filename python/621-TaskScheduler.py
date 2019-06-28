# Time:
# Space:

# Given a char array representing tasks CPU need to do. It contains
# capital letters A to Z where different letters represent different
# tasks.Tasks could be done without original order. Each task could
# be done in one interval. For each interval, CPU could finish one
# task or just be idle.
#
# However, there is a non-negative cooling interval n that means between
# two same tasks, there must be at least n intervals that CPU are doing
# different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take to
# finish all the given tasks.
#
# Example 1:
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # step 1
        # count the maximum value of the tasks
        counts = collections.defaultdict(int)
        for tsk in tasks:
            counts[tsk] += 1

        max_task = max(counts.values())

        # step 2
        # count the pre-arranged numbers
        ans = (1 + n) * (max_task - 1)

        # step 3
        # count how many tasks are there which has as many tasks as the maximum one
        for i in counts:
            if counts[i] == max_task:
                ans += 1

        return max(ans, len(tasks))


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "C", "C", "D", "D"]
    n = 2
    print(Solution().leastInterval(tasks, n))


