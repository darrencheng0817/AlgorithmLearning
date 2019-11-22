'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        currentBoard = ['.' * n for _ in range(n)]
        res = []
        self.helper(n, currentBoard, 0, res)
        return res

    def helper(self, n:int, currentBoard:List[str], currentRow:int, res: List[List[str]]):
        if currentRow == n:
            self.printBoard(currentBoard)
            res.append(self.deepcopy(currentBoard))
        for i in range(n):
            if self.check(currentBoard, currentRow, i):
                listRow = list(currentBoard[currentRow])
                listRow[i] = 'Q'
                currentBoard[currentRow] = ''.join(listRow)
                self.helper(n, currentBoard, currentRow + 1, res)
                currentBoard[currentRow] = '.' * n

    def deepcopy(self, currentBoard:List[str]) -> List[str]:
        res = []
        for i in range(len(currentBoard)):
            res.append(currentBoard[i])
        return res

    def check(self, currentBoard:List[str], currentRow:int, currentColumn: int) -> bool:
        for i in range(currentRow):
            if currentBoard[i][currentColumn] == 'Q':
                return False
        for i in range(1, currentRow + 1):
            if currentRow - i >= 0 and currentColumn - i >= 0:
                if currentBoard[currentRow - i][currentColumn - i] == 'Q':
                    return False
            if currentRow - i >= 0 and currentColumn + i < len(currentBoard):
                if currentBoard[currentRow - i][currentColumn + i] == 'Q':
                    return False
        return True

    def printBoard(self,currentBoard:List[str]):
        for i in range(len(currentBoard)):
            print(currentBoard[i])
        print()


s = Solution()
print(s.solveNQueens(9))
