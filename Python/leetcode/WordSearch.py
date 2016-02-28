'''
Created on 1.12.2016

@author: Darren
''''''

Given a 2D board and a word, find if the word exists in the grid.


The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.



For example,
Given board = 

[
  [ A , B , C , E ],
  [ S , F , C , S ],
  [ A , D , E , E ]
]


word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
" 
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        next_pos=[(0,1),(0,-1),(-1,0),(1,0)]
        def find(i,j,index,visited):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            if board[i][j]==word[index]:
                for k in range(len(next_pos)):
                    new_i,new_j=i+next_pos[k][0],j+next_pos[k][1]
                    if (new_i,new_j) not in visited:
                        visited.add((new_i,new_j))
                        if find(new_i,new_j,index+1,visited):
                            return True
                        visited.remove((new_i,new_j))
            else:
                return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited=set()
                visited.add((row,col))
                if find(row,col,0,visited):
                    return True
        return False
    
so=Solution()
board=["ABCE","SFCS","ADEE"]
word="ABCCED"
print(so.exist(board, word))