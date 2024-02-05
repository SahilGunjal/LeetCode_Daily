"""
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
# Intuition: Intuition is easy first count the occurrence of each letter and then check again the first char without
# repetition

# Time and Space - O(n) - n: size of string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = Counter(s)

        for index, char in enumerate(s):
            if my_dict[char] == 1:
                return index

        return -1

