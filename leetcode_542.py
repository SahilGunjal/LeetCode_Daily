"""

Intuition: Use bfs to traverse and start with 0's put all of them in the que with distance 0 in the begining.
TC: O(4*m*n)
SC : O(2m*n)
"""

# Previous Solution:
from collections import deque


class Solution:

    def calculate_distance(self, mat, visited, distance, rows, cols):
        que = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    que.append((i, j, 0))
                    visited[i][j] = 1
                    distance[i][j] = 0

        while que:
            curr = que.popleft()
            i = curr[0]
            j = curr[1]
            temp_distance = curr[2]
            distance[i][j] = temp_distance

            if i - 1 >= 0:
                if visited[i - 1][j] == 0:
                    visited[i - 1][j] = 1
                    que.append((i - 1, j, temp_distance + 1))

            if i + 1 < rows:
                if visited[i + 1][j] == 0:
                    visited[i + 1][j] = 1
                    que.append((i + 1, j, temp_distance + 1))

            if j - 1 >= 0:
                if visited[i][j - 1] == 0:
                    visited[i][j - 1] = 1
                    que.append((i, j - 1, temp_distance + 1))

            if j + 1 < cols:
                if visited[i][j + 1] == 0:
                    visited[i][j + 1] = 1
                    que.append((i, j + 1, temp_distance + 1))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for i in range(cols)] for j in range(rows)]
        distance = [[0 for i in range(cols)] for j in range(rows)]

        self.calculate_distance(mat, visited, distance, rows, cols)

        return distance


# Practice

class Solution:

    def calculate_the_ans(self, mat, visited, distance):

        que = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.append((i, j, 0))
                    visited[i][j] = 1

        arr_row = [-1, 0, +1, 0]
        arr_col = [0, +1, 0, -1]
        while que:
            curr = que.popleft()
            i = curr[0]
            j = curr[1]
            dist = curr[2]
            distance[i][j] = dist

            for k in range(4):
                nrow = i + arr_row[k]
                ncol = j + arr_col[k]

                if (nrow >= 0 and nrow < len(mat) and ncol >= 0 and ncol < len(mat[0])):
                    if visited[nrow][ncol] == 0:
                        visited[nrow][ncol] = 1
                        que.append((nrow, ncol, dist + 1))

        return distance

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        distance = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]

        return self.calculate_the_ans(mat, visited, distance)

