"""
1048. Longest String Chain
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing
the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""

# Intuition: This is the version of the LIS. Just use comparator and sort it as they are not asking subsequence,
# they want sequence in any order, sort it to solve the order.

# TC - O(n^2)*(size of the string_i)
# SC - O(n)


class Solution:
    def compare(self, string1, string2):
        if len(string1) != (len(string2) + 1):
            return False

        ptr1 = 0
        ptr2 = 0

        while (ptr1 < len(string1)):
            if ptr2 < len(string2) and string1[ptr1] == string2[ptr2]:
                ptr1 += 1
                ptr2 += 1

            else:
                ptr1 += 1

        if ptr1 == len(string1) and ptr2 == len(string2):
            return True

        return False

    def longestStrChain(self, words: List[str]) -> int:
        arr = sorted(words, key=len)

        dp = [1] * len(arr)
        maxi = 1
        for i in range(len(arr)):
            for j in range(i):
                if self.compare(arr[i], arr[j]) and (dp[i] < dp[j] + 1):
                    dp[i] = dp[j] + 1

            maxi = max(dp[i], maxi)

        return maxi



