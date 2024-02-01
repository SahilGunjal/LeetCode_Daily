"""
2966. Divide Array Into Arrays With Max Difference

You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following conditions:

Each element of nums should be in exactly one array.
The difference between any two elements in one array is less than or equal to k.
Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array.
And if there are multiple answers, return any of them.

# Intuition: Initially check if there no n factor element in array return empty. Then iterate through sorted array
# and check if the entering element - first element in the array group is less than equal k
"""

# Time - O(n)
# Space - Solution consider then O(n)

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        if n % 3 != 0:
            return []

        nums.sort()
        print(nums)
        ans = [[] for i in range(n // 3)]
        arr_ind = 0

        for num in nums:
            if len(ans[arr_ind]) == 0:
                ans[arr_ind].append(num)

            else:
                if num - ans[arr_ind][0] <= k:
                    ans[arr_ind].append(num)

                    if len(ans[arr_ind]) == 3:
                        arr_ind += 1

                else:
                    return []

        return ans







