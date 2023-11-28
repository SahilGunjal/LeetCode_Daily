"""
935. Knight Dialer
The chess knight has a unique movement, it may move two squares vertically and one square horizontally,
or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:
"""


class Solution:
    def knightDialer(self, n: int) -> int:

        def recursive(i, j, k, dp):
            if (i < 0 or i > 3) or (j < 0 or j > 2):
                return 0

            if (i == 3 and j == 0) or (i == 3 and j == 2):
                return 0

            if k == 1:
                if (i == 3 and j == 0) or (i == 3 and j == 2):
                    return 0
                else:
                    return 1

            if (i, j, k) in dp:
                return dp[i, j, k]

            possible_num = 0

            delta = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

            for delta_row, delta_col in delta:
                new_i = delta_row + i
                new_j = delta_col + j
                possible_num += recursive(new_i, new_j, k - 1, dp)

            dp[(i, j, k)] = (possible_num) % (10 ** 9 + 7)
            return dp[(i, j, k)]

        temp = 0
        dp = {}
        for i in range(4):
            for j in range(3):
                if (i == 3 and j == 0) or (i == 3 and j == 2):
                    continue
                else:
                    temp += recursive(i, j, n, dp)

        return temp % (10 ** 9 + 7)
