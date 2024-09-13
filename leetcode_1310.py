"""
1310. XOR Queries of a Subarray

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.
"""

# Approach: First calculate continous xor of all elements in the array. Then as per queries do xor again.
# Time complexity = max(O(queries), O(array))
# Space Complexity = O(array)

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor_arr = []

        for i in range(len(arr)):
            if i == 0:
                xor_arr.append(arr[0])
            else:
                xor_arr.append(xor_arr[-1] ^ arr[i])

        ans = []

        for ind1, ind2 in queries:
            if ind1 == 0:
                ans.append(xor_arr[ind2])
            else:
                ans.append(xor_arr[ind2] ^ xor_arr[ind1 - 1])

        return ans


