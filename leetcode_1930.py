"""
1930. Unique Length-3 Palindromic Subsequences
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
"""

# Naive Approach : Generate all subsequence of length 3 and then check if they are palindrome

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        def recursive(ind, strr):
            # This must be the first condition else it will not generate all combinations
            if len(strr) == 3:
                if strr[0] == strr[2]:
                    my_set.add(strr)
                return
                # this must be the second condition
            if ind >= len(s):
                return

            strr += s[ind]
            recursive(ind + 1, strr)
            strr = strr[:-1]
            recursive(ind + 1, strr)

        my_set = set()
        ind = 0
        recursive(ind, '')
        print(my_set)
        return len(my_set)


# Slightly better time complexity code using hash

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        my_dict = {}
        total_str = set()
        final_ans = 0
        for i, char in enumerate(s):
            if char not in my_dict:
                my_dict[char] = (1, i)

            else:
                count, index = my_dict[char]
                count += 1
                my_dict[char] = (count, i)
                if count == 3:
                    final_ans += 1

                if i != index + 1:
                    temp_str = s[index + 1: i]
                    subset = set(temp_str)
                    count = 0
                    for c in subset:
                        temp = s[i] + c + s[i]
                        if temp not in total_str:
                            total_str.add(temp)
                            count += 1
                    final_ans += count

        return final_ans



