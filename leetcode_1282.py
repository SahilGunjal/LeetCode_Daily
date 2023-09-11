"""
1282. Group the People Given the Group Size They Belong To
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from
0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in.
For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers,
return any of them. It is guaranteed that there will be at least one valid solution for the given input.
"""


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        This solution is easy and good but taking 2 for loops and there is inner loop too to put the
        elements in the another lists
        ans = []
        my_dict = defaultdict(list)
        for i in range(len(groupSizes)):
            my_dict[groupSizes[i]].append(i)

        # print(my_dict)
        for key,values in my_dict.items():
            if len(values) == key:
                ans.append(values)
            else:
                no_of_lists = len(values)//key
                # print(no_of_lists)
                start = 0
                end = key
                for i in range(no_of_lists):
                    ans.append(values[start:end])
                    start = end
                    end = end + key

        return ans

        # This can Also be done in one loop and hashtable as follows:
        # Tc: O(n)
        # SC: O(n)

        my_dict = {}

        ans = []

        for i, size in enumerate(groupSizes):
            if size not in my_dict:
                my_dict[size] = []
                my_dict[size].append(i)
            else:
                my_dict[size].append(i)

            if size == len(my_dict[size]):
                ans.append(my_dict[size])
                my_dict[size] = []

        return ans
