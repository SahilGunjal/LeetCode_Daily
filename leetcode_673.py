"""
leetcode: 673. Number of Longest Increasing Subsequence
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.
Intuition: This is very similar to longest increasing subsequence problem. Just take another array for count and
if dp[j]+1 > dp[i] then make count of i and j similar and if they are equal then add their count values.
Find the maximum LIS of nums from dp and add count of those and return count_longest_increasing_subsequence.
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1]*size
        cnt = [1]*size
        max_lis = float('-inf')
        for i in range(size):
            for j in range(0,i):
                if nums[i]>nums[j] and dp[i]< dp[j]+1:
                    dp[i] = dp[j]+1
                    cnt[i] = cnt[j]
                elif nums[i]>nums[j] and dp[i] == dp[j]+1:
                    cnt[i] += cnt[j]

            max_lis = max(max_lis,dp[i])

        count_longest = 0
        for i in range(size):
            if dp[i] == max_lis:
                count_longest += cnt[i]


        return count_longest
