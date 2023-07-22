"""
688. Knight Probability in Chessboard

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal
direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go
off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

"""

class Solution:
    def probab(self, n, k, rows, cols, directions, my_dict):
        if rows < 0 or rows >= n or cols < 0 or cols >= n:
            return 0

        if k == 0:
            return 1

        my_key = str(rows) + '-' + str(cols) + '-' + str(k)
        if my_key in my_dict:
            return my_dict[my_key]

        p = 0
        for i in range(8):
            p = p + self.probab(n, k - 1, directions[i][0] + rows, directions[i][1] + cols, directions, my_dict) / 8

        my_dict[my_key] = p
        return my_dict[my_key]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
        my_dict = dict()
        return self.probab(n, k, row, column, directions, my_dict)

