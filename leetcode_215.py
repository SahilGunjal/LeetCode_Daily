"""
Leetcode: 215 : Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
# Approach 1: Without extra space

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        smallest = len(nums) - k + 1

        def partition(l, r):
            i = l
            val = nums[r]
            for j in range(l, r):
                if nums[j] <= val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]

            return i

        def kselect(l, r):

            index = partition(l, r)
            # print(index)

            if index + 1 == smallest:
                return nums[index]

            elif smallest < index + 1:
                return kselect(l, index - 1)

            else:
                return kselect(index + 1, r)

        return kselect(0, len(nums) - 1)


# Using Extra 3 lists left, right, mid

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def kselect(arr, k):
            left = []
            mid = []
            right = []

            pivot = random.choice(arr)

            for num in arr:
                if num > pivot:
                    left.append(num)

                elif num < pivot:
                    right.append(num)

                else:
                    mid.append(num)

            if k <= len(left):
                return kselect(left, k)

            elif k > len(left) + len(mid):
                return kselect(right, k - len(mid) - len(left))

            return pivot

        return kselect(nums, k)


