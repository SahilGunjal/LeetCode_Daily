"""
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Intuition: Initially find the k (where the split/rotation happend) - Do that using the binary search only using last
element of the nums array and then apply bSearch twice.
TC - O(3logn)
SC - O(logn) stack space of the recursion
"""


class Solution:

    def searchK(self, l, r, nums):

        if r >= l:
            mid = l + (r - l) // 2

            if nums[mid] > nums[-1]:
                return self.searchK(mid + 1, r, nums)
            else:
                return self.searchK(l, mid - 1, nums)

        else:
            return l

    def bSearch(self, l, r, nums, target):
        if r >= l:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                return self.bSearch(l, mid - 1, nums, target)

            else:
                return self.bSearch(mid + 1, r, nums, target)

        return -1

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        k = self.searchK(0, len(nums) - 1, nums)
        print(k)
        ans = self.bSearch(0, k - 1, nums, target)
        if ans != -1:
            return ans
        return self.bSearch(k, len(nums) - 1, nums, target)
