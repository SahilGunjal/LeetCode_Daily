"""
1218. Longest Arithmetic Subsequence of Given Difference
Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an
arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the
order of the remaining elements.

Intuition :(DP + Hash) This is a 1-D DP problem and we have to use hash table or dictionary for this as well
for each element we simply have to check whether this element were present in the dictionary if yes take its value
add it with 1 and push that in dictionary for the current element, else just push 1 for the current element.
At the end calculate the maximum of the all dictionary values and return it.
"""

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [0] * len(arr)
        maxDict = dict()

        for num in arr:
            val = num - difference
            if val in maxDict:
                maxDict[num] = 1 + maxDict[val]
            else:
                maxDict[num] = 1

        return max(maxDict.values())