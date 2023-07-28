"""
Leetcode: 486. Predict the Winner
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each
turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which
reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no
more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner,
and you should also return true. You may assume that both players are playing optimally.

Intuition: player can take from either left or right and rest part we should repeat the same process again and
again so, use recursion plus if we are taking from the left then we can add it, and whatever second player is
getting we can subtract it as we have to calculate for one player only and if the playes's total at the end is >=0
means player wins > is fine but =0 because even if both player got same score still player 1 is winner.
we are using dp simply to store all the values so that we dont have to recalculate it.
complexity : ~ o(n^2)
"""

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        has_element = [[False] * (n) for i in range(n)]
        dp = [[None] * (n) for i in range(n)]

        def calculateWinner(l, r):
            if l > r:
                return 0

            if has_element[l][r]:
                return dp[l][r]

            left_sum = nums[l] - calculateWinner(l + 1, r)
            right_sum = nums[r] - calculateWinner(l, r - 1)

            has_element[l][r] = True
            dp[l][r] = max(left_sum, right_sum)

            return dp[l][r]

        return calculateWinner(0, n - 1) >= 0


