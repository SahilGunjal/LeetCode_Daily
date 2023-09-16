"""
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where
heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you
hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right,
 and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Intuition: In this case I am using min heap and bfs to find the min_efforts.
"""

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        r = len(heights)
        c = len(heights[0])

        if len(heights) == 0:
            return 0
        visited = set()
        que = [(0, 0, 0)]

        heapq.heapify(que)
        visited = set()
        min_effort = 0

        while que:
            curr_effort, i, j = heapq.heappop(que)
            visited.add((i, j))
            rows = [-1, 0, +1, 0]
            cols = [0, +1, 0, -1]

            min_effort = max(min_effort, curr_effort)

            if i == r - 1 and j == c - 1:
                return min_effort

            for direc in range(len(rows)):
                curr_i = i + rows[direc]
                curr_j = j + cols[direc]
                if curr_i < r and curr_i >= 0 and curr_j >= 0 and curr_j < c and (curr_i, curr_j) not in visited:
                    heapq.heappush(que, (abs(heights[i][j] - heights[curr_i][curr_j]), curr_i, curr_j))

        return min_effort






