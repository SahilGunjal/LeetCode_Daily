"""
287. Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

# Intuition: It is very similar to detecting the cycle in the linkedList but with little modification. Once the
# Slow ptr and fastptr meets then we need to again start the checking from the nums[0] and slow_ptr.

# It is also known as floyd's tortoise approch
# Time complexity O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = nums[0]
        fast_ptr = nums[0]

        while True:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]

            if slow_ptr == fast_ptr:
                break

        temp = nums[0]
        while temp != slow_ptr:
            slow_ptr = nums[slow_ptr]
            temp = nums[temp]

        return temp

