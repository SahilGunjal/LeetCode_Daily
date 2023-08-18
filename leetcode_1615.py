"""
1615. Maximal Network Rank
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi]
indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city.
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Intuition: Simple logic degree(u) + degree(v) - f(u,v) and if there is link between u and v then f(u,v) = 1 else 0.

TC: O(n*n)
SC: O(n*n)
"""

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0 for i in range(n)]
        graph = [[False] * n for i in range(n)]

        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1
            graph[road[0]][road[1]] = True
            graph[road[1]][road[0]] = True

        max_rank = float('-inf')
        for i in range(n - 1):
            for j in range(i + 1, n):
                curr_rank = degree[i] + degree[j]

                if graph[i][j] == True:
                    curr_rank -= 1

                max_rank = max(curr_rank, max_rank)

        return max_rank










