"""
Leetcode: 802 - Find Eventual Safe state
"""

class Solution:
    def dfs(self, start, path_visited, visited, safe_state, graph):
        visited[start] = 1
        path_visited[start] = 1

        for neighbor in graph[start]:
            if visited[neighbor] == 0:
                if self.dfs(neighbor, path_visited, visited, safe_state, graph):
                    return True

            elif visited[neighbor] == 1 and path_visited[neighbor] == 1:
                return True

        path_visited[start] = 0
        safe_state[start] = 1

        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0 for i in range(n)]
        path_visited = [0 for i in range(n)]
        safe_state = [0 for i in range(n)]

        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, path_visited, visited, safe_state, graph)

        ans = []
        for i in range(n):
            if safe_state[i] == 1:
                ans.append(i)

        return ans