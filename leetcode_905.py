"""
905. Sort Array By Parity

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""

# runs good with the time ~O(n) and space O(1)


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = len(nums) - 1

        while ptr1 < ptr2:

            while ptr1 < ptr2 and nums[ptr1] % 2 == 0:
                ptr1 += 1
            while ptr1 < ptr2 and nums[ptr2] % 2 != 0:
                ptr2 -= 1

            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]

        return nums

# Another solution: O(n) and Space - O(n)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        e = []
        o = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                e.append(nums[i])
            else:
                o.append(nums[i])

        e += o
        return e

