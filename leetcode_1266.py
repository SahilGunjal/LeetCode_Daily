"""
1266. Minimum Time Visiting All Points

On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in
seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.

"""
# Time complexity : O(len(points))
# Space Complexity : O(1)
# Intuition: Initially I though I can use euclidean distance, but it wasn't giving the correct ans when I dry run it.
# Then I thought about the grid and then dry run it on the examples and it gave correct ans.
# Sum (Max(x_delta, y_delta)) consecutive points


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_distance = 0

        if len(points) <= 1:
            return 0
        for i in range(len(points) - 1):
            x1, y1 = points[i][0], points[i][1]
            x2, y2 = points[i + 1][0], points[i + 1][1]

            x_delta = abs(x2 - x1)
            y_delta = abs(y2 - y1)

            if x_delta >= y_delta:
                total_distance += x_delta
            else:
                total_distance += y_delta

        return total_distance
