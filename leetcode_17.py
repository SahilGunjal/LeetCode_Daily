"""
Leetcode 17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Intuition: Can use queue so the we can get the previously added elements and can add new elements again to it.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        my_dict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        letters = []
        for c in digits:
            letters.append(my_dict[c])

        if len(letters) == 1:
            return my_dict[digits[0]]

        # Using Queue for all combinations
        que = deque()
        que.append('')
        for lists in letters:
            new_que = deque()

            while que:
                curr = que.popleft()

                for chars in lists:
                    new_combo = curr + chars
                    new_que.append(new_combo)

            que = new_que

        return que


