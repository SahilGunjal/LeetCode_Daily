"""
Leetcode: Course Schedule : TopoSort
"""
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        topo = []
        que = deque()

        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])

        for i in range(len(adj)):
            for neighbor in adj[i]:
                indegree[neighbor] += 1

        for i in range(len(indegree)):
            if indegree[i] == 0:
                que.append(i)

        while que:
            curr = que.popleft()
            topo.append(curr)
            for neighbors in adj[curr]:
                indegree[neighbors] -= 1

                if indegree[neighbors] == 0:
                    que.append(neighbors)

        if len(topo) == numCourses:
            return True

        else:
            return False



