"""
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and
initial word order.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = list(map(str, s.split(' ')))

        for i,word in enumerate(wordList):
            wordList[i] = word[::-1]

        # print(wordList)
        return ' '.join(wordList)