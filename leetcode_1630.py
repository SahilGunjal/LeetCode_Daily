"""
 Arithmetic Subarrays
 You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m
 range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... ,
nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.

"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def check_AP(temp):
            diff = temp[1] - temp[0]
            for i in range(1, len(temp) - 1):
                if temp[i + 1] - temp[i] != diff:
                    return False

            return True

        ans = []
        for i in range(len(l)):
            start = l[i]
            end = r[i] + 1
            temp = sorted(nums[start:end])

            if check_AP(temp):
                ans.append(True)
            else:
                ans.append(False)

        return ans


