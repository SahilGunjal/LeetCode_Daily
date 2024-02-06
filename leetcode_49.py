"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

"""

# Intuition: If we sort the each word and make them as key and use defaultdict(list) to append the same elements.
# Space: o(n)
# Time: O(n * (word_size)log(word_size))

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for word in strs:
            new_word = ''.join(sorted(word))
            my_dict[new_word].append(word)

        return list(my_dict.values())