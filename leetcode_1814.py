"""
1814. Count Nice Pairs in an Array
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the
non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Intuition: We can make equation nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]), So go on calculating this and adding
it in the dictionary with the count, as we want pairs that's why count is imp and if same subtraction comes up,
increase the count of nice_pairs as per the count of that value and then again add the value count in the dict.
Time and Space complexity : O(n*(no of digit in the number)) and space O(len(nums))
"""

import math


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def reverse_num(num):
            reversed_num = 0
            while num > 0:
                reversed_num = (reversed_num * 10) + (num % 10)
                num = num // 10

            return reversed_num

        mod_factor = math.pow(10, 9) + 7
        my_set = {}
        nice_numbers = 0
        for num in nums:
            temp = num - reverse_num(num)
            if temp not in my_set:
                my_set[temp] = 1
            else:
                nice_numbers += my_set[temp]
                my_set[temp] += 1

        return int(nice_numbers % mod_factor)
