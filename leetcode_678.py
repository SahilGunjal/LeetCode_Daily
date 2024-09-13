"""
678. Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
"""

# Recursive Solution is very simple. I just assumed that ( means 1, ) means -1 and * can be +1, -1 or none.
# But while converting this solution to Dp we can easily traverse the ind but how to traverse the count variable, because
# Count is not fix. That's the only issue in this solution while converting recursive to dp.

class Solution:
    def checkValidString(self, s: str) -> bool:
        def recursive(ind, count):
            if ind == len(s):
                if count == 0:
                    return True
                else:
                    return False

            first = False
            if s[ind] == '(':
                count += 1
                first = recursive(ind + 1, count)

            second = False
            if s[ind] == ')':
                if count > 0:
                    count -= 1
                    second = recursive(ind + 1, count)

            third = False
            if s[ind] == '*':
                third = recursive(ind + 1, count) or recursive(ind + 1, count + 1) or recursive(ind + 1, count - 1)

            return first or second or third

        return recursive(0, 0)
