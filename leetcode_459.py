"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the
substring together.

Intuition: we know that length of substring must divide string s completely only consider that much and check if
each substring till n//2 forms a substring or not if yes return True else return false.
TC: O(n*sq(n))
SC: O(n)
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sub = s[:i]
                if s == sub * (n // i):
                    return True

        return False

"""
Another Solution:
TC : O(n): Adding two strings and finding the substring in that. 
Intuition: Return true if we add two strings and if s is in [1:-1] of two added strings then return true else
return false. 
"""
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]