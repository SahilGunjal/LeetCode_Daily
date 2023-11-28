"""
2147. Number of Ways to Divide a Long Corridor
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string
 corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1.
 Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of
plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7.
If there is no way, return 0.

"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = corridor.count('S')

        if n < 2 or n % 2 != 0:
            return 0

        temp_list = []
        s_count = 0
        total = 0
        start_ind = 0
        start = None
        end = None
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                s_count += 1

            if s_count == 2:
                start = i
                start_ind = i + 1
                break

        for i in range(start_ind, len(corridor)):

            if corridor[i] == 'S':
                s_count += 1
                if s_count % 2 == 1:
                    end = i
                    temp_val = end - start
                    temp_list.append(temp_val)

                if s_count % 2 == 0:
                    start = i

        possible_ways = 1
        for temp in temp_list:
            possible_ways *= temp

        return possible_ways % (10 ** 9 + 7)




