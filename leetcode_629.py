"""
629. K Inverse Pairs Array

Problem Statement: For an integer array nums, an inverse pair is a pair of integers [i, j] where
0 <= i < j < nums.length and nums[i] > nums[j].
Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there
are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Intuition: It's definitely a hard problem.
1. Recursive: As we need to see all the arrays and all possible values for each k.
2. let's say n = 3
___ for first position we can put 2 values. and depend on which value we put we get the value of k.
for example if we put k == 1 at first position then we know we won't be able to form any inverse pair as it's the
smallest value. if we put 2 then we are able to form 1 as 2 is smaller than just 1. (so one inverse pair.)
If we put 3 then inverse pairs will be 2. So we just keep subtracting the k and run recursive.

## This part is not that intuitive.

Then build the recursive solution and then memoize and convert it into dp solution.
(This still doesn't work.)
# If we see then we can use sliding window in this problem! And then only it get's accepted.
"""


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # def recursive(n, k):
        #     if n == 0:
        #         if k == 0:
        #             return 1
        #         else:
        #             return 0

        #     if k < 0:
        #         return 0

        #     if (n,k) in dp:
        #         return dp[(n,k)]

        #     total_array = 0
        #     for i in range(n):
        #         total_array += recursive(n-1, k-i)

        #     dp[(n,k)] = total_array % mod_val
        #     return dp[(n,k)]

        # dp = dict()

        # return recursive(n, k)

        mod_val = 10 ** 9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            curr = [0] * (k + 1)
            total_array = 0
            for j in range(0, k + 1):
                if j >= i:
                    total_array -= prev[j - i]

                total_array = (total_array + prev[j]) % mod_val

                curr[j] = total_array

            prev = curr.copy()

        return prev[k]

