"""
168. Excel Sheet Column Title
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Intuition: If we see characters are repeating after 26, so we can solve it using base 26. The only question is that
we have A-Z as 0-25 and given 1-26 so we have to subtract the -1 from the columnNumber and then calculate the
char for that curr. and then divide the columnNumber by 26. continue this until columnNumber is 0.

SC- O(1)
TC - O(log26n) log base:26
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''

        while columnNumber != 0:
            columnNumber -= 1

            curr = columnNumber % 26

            ans += chr(ord('A') + curr)

            columnNumber = columnNumber // 26

        return ans[::-1]



