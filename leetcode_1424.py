"""
1424. Diagonal Traverse II
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.
"""

# TC: O(n)

from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        my_dict = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i]))
                temp = nums[j][i]
                my_dict[temp].append(value)

        ans = []

        for key, values in my_dict.items():
            ans.extend(values)

        return ans
