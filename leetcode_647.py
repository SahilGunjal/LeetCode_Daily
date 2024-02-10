"""
647. Palindromic Substrings
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

# It was little tricky to solve but palindrome means the string in reverse order also gives the same string.
# we can iterate through each character and then go on checking the left and right if they are same then increase
# the count else break. But in this case we will miss the even elements so we have to consider them as well.

# time complexity = O(n^2)

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            prev = i
            nexxt = i
            while prev >= 0 and nexxt < n:
                if s[prev] == s[nexxt]:
                    count += 1
                    prev -= 1
                    nexxt += 1
                else:
                    break

        i = 0
        while i < n:
            prev = i
            nexxt = i + 1
            while prev >= 0 and nexxt < n:
                if s[prev] == s[nexxt]:
                    count += 1
                    prev -= 1
                    nexxt += 1
                else:
                    break
            i += 1

        return count

