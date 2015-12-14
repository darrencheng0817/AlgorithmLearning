'''
Created on 2015年12月1日
https://leetcode.com/problems/word-ladder/
@author: Darren
'''

def wordLadder(startWord,endWord,wordDic,path,visited):
    pass
def wordLadder2(startWord,endWord,wordDic,path,visited,res):
    pass
startWord="hit"
endWord="cog"
wordDic=["hot","dot","dog","lot","log"]
print("->".join(wordLadder(startWord, endWord, wordDic, ["hit"],set())))
res=[]
wordLadder2(startWord, endWord, wordDic, [startWord], set(), res)
print(res)
for item in res:
    print("->".join(item))