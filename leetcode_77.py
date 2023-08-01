"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Intuition: As we see subsequence or combinations start thinking about the recursion. And when we have to pick
something from the array start thinking about pick and non pick method.
calculate all combinations and at the end see if combinations with len == k
return ans
"""

class Solution:
    def calculateCombinations(self, ind, n, ans, temp):
        if ind > n:
            ans.append(temp.copy())
            return

        temp.append(ind)
        self.calculateCombinations(ind + 1, n, ans, temp)
        temp.pop()
        self.calculateCombinations(ind + 1, n, ans, temp)

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        ans = []
        final_ans = []

        self.calculateCombinations(1, n, ans, [])
        # print(ans)

        for lists in ans:
            if len(lists) == k:
                final_ans.append(lists)

        return final_ans
