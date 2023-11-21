"""
2391. Minimum Amount of Time to Collect Garbage

You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith
house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass
garbage respectively. Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house
i to house i + 1.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck
starts at house 0 and must visit each house in order; however, they do not need to visit every house.

Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other
two trucks cannot do anything.

Return the minimum number of minutes needed to pick up all the garbage.


Intuition: Took all the G,P,M and their house no in the dictionary. And then based on the house no and the travel array
calculated the total_minimum_time.

Time complexity : O(2(3* total house)) ~ worst case
Space Complexity : O(3 * total_house)
"""

from collections import defaultdict


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        my_dict = defaultdict(list)

        for house_no, items in enumerate(garbage):
            for garbage_type in items:
                my_dict[garbage_type].append(house_no)

        total_min = 0
        for key, values in my_dict.items():
            temp_min = 0
            curr_position_truck = 0
            for house_no in values:
                if house_no == 0:
                    temp_min += 1

                else:
                    temp_min += sum(travel[curr_position_truck: house_no])
                    temp_min += 1
                    curr_position_truck = house_no

            total_min += temp_min

        return total_min

