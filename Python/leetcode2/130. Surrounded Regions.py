'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''

from queue import Queue


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        q = Queue()
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    q.put((i, j))
        for i in range(len(board)):
            for j in [0, len(board[0]) - 1]:
                if board[i][j] == 'O':
                    q.put((i, j))
        while q.qsize()>0:
            i, j = q.get()
            board[i][j] = "#"
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]) and board[i + di][j + dj] == "O":
                    q.put((i + di, j + dj))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        print(board)

s = Solution()
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))