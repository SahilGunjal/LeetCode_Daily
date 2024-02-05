"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring,
 return the empty string "".

The testcases will be generated such that the answer is unique.

"""

# Intuition - Given array/ string. to calculate - window size
# problem - sliding window of variable size
# Solution - Tricky part here is to keep the count. We know for each interval we need to check whether all elements a
# present or not. We can keep the count for it.
# if dict[char] == 0 then decrease the count. and once the count is zero then check if we can shorten the string.(keeping)
# count == 0 if count > 1 then again move the index.
# Repeat this


# Time complexity - O(n) - n: len(s)
# Space complexity - o(t) - t: len(s)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if len(t) > len(s):
        #     return
        my_dict = Counter(t)
        smallest_string = ''
        j = 0
        count = len(my_dict)
        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] -= 1
                if my_dict[s[i]] == 0:
                    count -= 1

                if count == 0:
                    while count == 0:
                        temp_str = s[j: i + 1]
                        if smallest_string == '' or len(temp_str) < len(smallest_string):
                            smallest_string = temp_str

                        if s[j] in my_dict:
                            my_dict[s[j]] += 1

                        if my_dict[s[j]] > 0:
                            count += 1

                        j += 1

        return smallest_string










