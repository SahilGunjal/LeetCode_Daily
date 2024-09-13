"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

So, I tried this very easy method for this - simple dfs and was checking the distance if it's less than threshold then
was adding it to the total cities that can be covered by this city. But, let's draw the following example
n = 6
edges = [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]]
threshold = 20

Why Other approach Dijkstra's: when we draw this we notice that from zero if we use dfs we can cover only 4 as we are marking cities as visited.
but, In actual we can cover all those 5 cities. So, we need dp to think which to take and which edge to not take.
This makes the problem statement a bit tricky.
"""

# Failed Approach
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        def dfs(city, total_cities, distance, visited, graph):
            visited.add(city)

            for neigh, dist in graph[city]:
                next_dist = distance + dist
                if next_dist <= distanceThreshold and neigh not in visited:
                    total_cities[0] += 1
                    dfs(neigh, total_cities, next_dist, visited, graph)

            return total_cities[0]

        graph = dict()
        for u, v, dist in edges:
            if u in graph:
                graph[u].append([v, dist])
            else:
                graph[u] = []
                graph[u].append([v, dist])

            if v in graph:
                graph[v].append([u, dist])

            else:
                graph[v] = []
                graph[v].append([u, dist])

        no_of_cities = [0 for i in range(n)]
        print(graph)
        ans = float('inf')
        final_ans = -1
        for i in sorted(graph.keys()):
            visited = set()
            no_of_cities[i] = dfs(i, [0], 0, visited, graph)
            if no_of_cities[i] <= ans:
                final_ans = i
                ans = no_of_cities[i]

        print(no_of_cities)
        tt = final_ans
        for i in range(n):
            if i not in graph and i > tt:
                tt = i
        return tt

# Correct Approach

