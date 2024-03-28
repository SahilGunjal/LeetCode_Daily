"""
2958. Length of Longest Subarray With at Most K Frequency

You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

# This is simple sliding window problem with variable size window. Here we have given the constraint that the count of
# any number in particular window should not exceed the k, and we have to find the maximum window size.

# Time complexity: O(n)

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = dict()

        longest_sub = -float('inf')

        i = -1
        j = 0

        while j < len(nums):
            if nums[j] in count and count[nums[j]] + 1 > k:
                i += 1
                while nums[i] != nums[j]:
                    count[nums[i]] -= 1
                    i += 1

                count[nums[i]] -= 1

            if nums[j] not in count:
                count[nums[j]] = 1

            else:
                count[nums[j]] += 1

            longest_sub = max(longest_sub, (j - i))

            j += 1

        return longest_sub

