"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

# Approach : Recursion and using one extra visited Array
# TC - o(n!)*n
# SC - o(n) - extra visited array and o(n) - auxiliary stack space


class Solution:
    def calPermutations(self, nums, temp, allPermutations, visited):
        if len(temp) == len(nums):
            allPermutations.append(temp.copy())
            return

        for i in range(len(nums)):
            if visited[i] == 0:
                temp.append(nums[i])
                visited[i] = 1
                self.calPermutations(nums, temp, allPermutations, visited)
                temp.pop()
                visited[i] = 0

    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []
        temp = []
        visited = [0] * len(nums)
        self.calPermutations(nums, temp, allPermutations, visited)

        return allPermutations


# Appraoch 2: Recursion using swapping the elements
# TC - O(n!)*n
# SC - auxiliary stack space - o(n)


class Solution:
    def calPermutations(self, ind, nums, allPermutations):
        if ind >= len(nums):
            allPermutations.append(nums.copy())
            return

        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            self.calPermutations(ind + 1, nums, allPermutations)
            nums[ind], nums[i] = nums[i], nums[ind]

    def permute(self, nums: List[int]) -> List[List[int]]:
        allPermutations = []
        self.calPermutations(0, nums, allPermutations)

        return allPermutations