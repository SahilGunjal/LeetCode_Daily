"""
2225. Find Players With Zero or One Losses
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated
player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
"""

# Approach: First store all the loser number and count in the dict. Then go through it once to get the list of defeated
# once. Again go through the matches and store the numbers which is unique and not in loser dict.
# sort both and return
# let n = len(matches)
# TC: O(3n) + O(2nlogn)
# SC: Worst - O(2n)

# solution
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_at_the_most_one = []
        lost_dict = dict()
        for match in matches:
            if match[1] not in lost_dict:
                lost_dict[match[1]] = 1

            else:
                lost_dict[match[1]] += 1

        for key, value in lost_dict.items():
            if value == 1:
                lost_at_the_most_one.append(key)

        not_lost_anything = []
        for match in matches:
            if match[0] not in lost_dict and match[0] not in not_lost_anything:
                not_lost_anything.append(match[0])

        ans = []
        ans.append(sorted(not_lost_anything))
        ans.append(sorted(lost_at_the_most_one))

        return ans





