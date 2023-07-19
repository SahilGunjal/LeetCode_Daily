"""
Leetcode: 435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.

Intuition: Very simple just use logic of basic interval scheduling algorithm. Sort the element based on
finish time and then use for loop to calculate the count.(Greedy) It gives the optimal answer.

TC: O(nlogn)- sorting based on finish time + O(n) : for for loop
SC: O(1) - No use of any extra space.(if sorting uses merge sort then it uses storage - O(n))
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])

        count = 1
        f_time = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] >= f_time:
                count += 1
                f_time = sorted_intervals[i][1]

        return len(sorted_intervals) - count




