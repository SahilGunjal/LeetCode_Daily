"""
2141. Maximum Running Time of N Computers

You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run
a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given
batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment,
you can remove a battery from a computer and insert another battery any number of times. The inserted battery
can be a totally new battery or a battery from another computer. You may assume that the removing and inserting
processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.


Intuition: Simple binary search, just note that those batteries who have min >= mid_min add them as mid_min and
rest add as direct battery min's and divide it by total computers and use this condition.
"""


class Solution:
    def ifPossible(self, n, batteries, mid_min):
        s = 0
        for b_min in batteries:
            if b_min >= mid_min:
                s += mid_min
            else:
                s += b_min

        return s / n

    def bSearch(self, n, batteries, l, r):
        max_min = 0
        while r >= l:
            mid_min = l + (r - l) // 2

            if self.ifPossible(n, batteries, mid_min) >= mid_min:
                max_min = mid_min
                l = mid_min + 1

            else:
                r = mid_min - 1

        return max_min

    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        max_min = self.bSearch(n, batteries, 1, sum(batteries))

        return max_min

