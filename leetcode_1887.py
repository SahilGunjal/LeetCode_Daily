"""
1887. Reduction Operations to Make the Array Elements Equal
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow
these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple
elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

"""
# Intuition : If we sort the array then we note that, we just have to take an addition of the elements from
# behind/forward till you hit the smallest element. For example 465. sort them 456 then take sum like 1 + 2  = 3.
# ex. 12233 then add 2 + 4 = 6 etc.

# Time complexity :  O(nlogn) + O(n) ~ O(nlogn)

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 0

            else:
                return 1

        nums.sort()
        print(nums)
        n = len(nums)
        min_element = nums[0]
        element = nums[-1]
        ind = n - 2
        temp = 1
        total_cost = 0
        flag = 0
        while nums[ind] != min_element:
            if nums[ind] < element:
                flag = 1
                element = nums[ind]
                total_cost += (n - (ind + 1))

            ind -= 1

        if flag == 0:
            if nums[ind] == nums[ind + 1]:
                return 0
            else:
                return (n - (ind + 1))
        else:
            total_cost += (n - (ind + 1))
            return total_cost









