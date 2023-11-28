"""
1727. Largest Submatrix With Rearrangements
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the
columns optimally.
"""

from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 1:
            return sum(matrix[0])

        rows = len(matrix)
        cols = len(matrix[0])

        temp = [[0] * cols for i in range(rows)]
        max_consecutive_row = 0
        max_consecutive_col = 0
        max_val = 0

        for i in range(cols):
            curr = 0
            for j in range(rows):
                if matrix[j][i] == 1:
                    curr += 1
                    temp[j][i] = curr
                else:
                    curr = 0
                    temp[j][i] = curr

        ans = 0
        for i in range(rows):
            temp[i].sort(reverse=1)
            for j in range(cols):
                ans = max(ans, (j + 1) * temp[i][j])

        return ans

