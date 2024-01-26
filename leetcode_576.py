"""
576. Out of Boundary Paths
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the
grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the
grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Approach: Build the recursive solution, and as we are moving 4 directions go and return the sum of all the ways.
Base case: if number of steps are 0 are if the ball is still inside the matrix then return 0, and if the ball is out of
the matrix and n>=0 then within max limit it was able to cross the boundary so consider that path.

Time complexity: O(4^(maxMoves*m*n)) - as for each step we have 4 options for each cell of the grid.
Space Complexity: O(maxMove * m * n)
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod_val = 10 ** 9 + 7

        def recursive(i, j, maxMove):
            if maxMove == 0:
                if (i >= 0 and i <= m - 1) and (j >= 0 and j <= n - 1):
                    return 0
                else:
                    return 1

            if (i < 0 or i >= m or j < 0 or j >= n) and maxMove >= 0:
                return 1

            if (i, j, maxMove) in dp:
                return dp[(i, j, maxMove)]

            delta_row = [-1, 0, +1, 0]
            delta_col = [0, +1, 0, -1]

            total = 0
            for k in range(4):
                temp_i = i + delta_row[k]
                temp_j = j + delta_col[k]
                total += recursive(temp_i, temp_j, maxMove - 1)

            dp[(i, j, maxMove)] = total % mod_val
            return dp[(i, j, maxMove)]

        dp = dict()
        return recursive(startRow, startColumn, maxMove)