"""
1870. Minimum Speed to Arrive on Time

You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to
the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where
dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on
the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach
the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal
point.

Intuition : Use binary search to check the min speed. for each min_speed check whether with this speed total_time
 required is less than hour or not if yes save it and move mid to left, else move to right.
"""

import math


class Solution:
    def total_time_required(self, dist, speed):
        t = 0

        for i in range(len(dist)):
            if i == len(dist) - 1:
                t += dist[i] / speed

            else:
                t += math.ceil((dist[i] / speed))

        return t

    def bSearch(self, l, r, min_speed, dist, hour):
        while r >= l:
            mid = l + (r - l) // 2

            if self.total_time_required(dist, mid) <= hour:
                min_speed = mid
                r = mid - 1
            else:
                l = mid + 1

        return min_speed

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        if math.ceil(hour) < len(dist):
            return -1

        l = 1
        r = 10 ** 7
        min_speed = -1

        return self.bSearch(l, r, min_speed, dist, hour)

