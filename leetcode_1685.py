"""
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation
of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
"""

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        ans = []
        Left_curr_sum = 0
        for i in range(n):
            l_sum = i * nums[i] - Left_curr_sum
            r_sum = (total_sum - Left_curr_sum - nums[i]) - (n - i - 1) * nums[i]

            Left_curr_sum += nums[i]
            ans.append(l_sum + r_sum)

        return ans
