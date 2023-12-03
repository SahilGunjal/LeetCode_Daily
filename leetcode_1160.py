"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
Time complexity:
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        my_set = {}

        for char in chars:
            if char not in my_set:
                my_set[char] = 1

            else:
                my_set[char] += 1

        total_len = 0
        for word in words:
            temp = my_set.copy()
            print(temp)
            flag = 0
            for char in word:
                if char in temp and temp[char] != 0:
                    temp[char] -= 1

                else:
                    flag = 1
                    break

            if flag == 0:
                total_len += len(word)

        return total_len

