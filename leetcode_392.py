"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        size_t = len(t)
        size_s = len(s)
        if size_s == 0:
            return True

        for i in range(size_t):
            if s[s_ptr] == t[i]:
                s_ptr += 1

            if s_ptr == size_s:
                return True

        return False

