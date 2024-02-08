"""
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer
with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""


"""
Both below solutions gave the TLE. :( 
"""
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # def recursive(ind, target):
        #     if ind <= val and target == 0:
        #         return 0

        #     if ind > val:
        #         if target == 0:
        #             return 0
        #         else:
        #             return float('inf')

        #     if (ind, target) in dp:
        #         return dp[(ind, target)]

        #     take = float('inf')
        #     if (ind*ind) <= target:
        #         take_leave = 1 + recursive(ind+1, target - (ind*ind))
        #         take_stay = 1 + recursive(ind, target - (ind*ind))
        #         take = min(take_leave, take_stay)

        #     nottake = recursive(ind+1, target)

        #     dp[(ind, target)] = min(take, nottake)
        #     return dp[(ind, target)]

        # val = int(math.sqrt(n))
        # dp = dict()
        # return recursive(1, n)

        val = int(math.sqrt(n))
        dp = [[0] * (n + 1) for i in range(val + 2)]

        for i in range(n + 1):
            if i != 0:
                dp[val + 1][i] = float('inf')

        for ind in range(val, 0, -1):
            for target in range(0, n + 1):
                take = float('inf')
                if (ind * ind) <= target:
                    take_leave = 1 + dp[ind + 1][target - (ind * ind)]
                    take_stay = 1 + dp[ind][target - (ind * ind)]
                    take = min(take_leave, take_stay)
                nottake = dp[ind + 1][target]

                dp[ind][target] = min(take, nottake)

        return dp[1][n]


# Most optimal solution:
# There is no need of considering the other part like for infinite taking i can stay at that index only and there is
# no need of checking it double. It will handle by other thing like not taking.

import math
class Solution:
    def numSquares(self, n: int) -> int:
        val = int(math.sqrt(n))
        dp = [[0]*(n+1) for i in range(val+2)]

        for i in range(n+1):
            if i != 0:
                dp[val+1][i] = float('inf')

        for ind in range(val, 0, -1):
            for target in range(0, n+1):
                take = float('inf')
                if (ind*ind) <= target:
                    take = 1 + dp[ind][target - (ind*ind)]

                nottake = dp[ind+1][target]

                dp[ind][target] = min(take, nottake)

        return dp[1][n]



