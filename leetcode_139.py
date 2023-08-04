"""
139. Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence
 of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Intuition: Add elements in que if till that letter word is in dict else continue and move the que till empty.
Time C - O(n^3) for checking and o(n) for putting words in set
Space c - (2n) - set and queue worst case
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words_set = set(wordDict)
        str_len = len(s)
        que = deque()
        que.append(0)
        visited = set()

        while que:
            begin = que.popleft()
            print(begin)

            if begin == str_len:
                return True

            for i in range(begin + 1, str_len + 1):
                if i in visited:
                    continue

                if s[begin:i] in words_set:
                    que.append(i)
                    visited.add(i)

        return False




