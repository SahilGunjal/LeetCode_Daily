"""
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at
any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

"""
Approach 1: use recursion and memoization
TC: O(2^m*n) and if use memoization O(m*n)
SC: O(m+n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = dict()

        def totalPaths(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1

            if (i, j) in dp:
                return dp[(i, j)]

            up = totalPaths(i - 1, j)
            left = totalPaths(i, j - 1)

            dp[(i, j)] = up + left

            return dp[(i, j)]

        return totalPaths(m - 1, n - 1)


"""
Approach 2: Use tabulation 
TC : O(m*n)
SC: O(m*n)
"""


def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = dp[i - 1][j] if i >= 1 else 0
                left = dp[i][j - 1] if j >= 1 else 0

                dp[i][j] = up + left

    return dp[m - 1][n - 1]


"""
Space Optimization:
we just need previous row and not the whole table
SC: O(m*n)
Tc: O(2n)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for i in range(n)] for j in range(m)]
        prev = [0 for i in range(n)]
        for i in range(m):
            curr = [0 for i in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = 1
                else:
                    up = prev[j] if i >= 1 else 0
                    left = curr[j - 1] if j >= 1 else 0

                    curr[j] = up + left

            prev = curr

        return prev[n - 1]
