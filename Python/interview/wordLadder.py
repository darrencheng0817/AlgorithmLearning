'''
Created on 2015年12月1日
https://leetcode.com/problems/word-ladder/
@author: Darren
'''

def wordLadder(startWord,endWord,wordDic,path,visited):
    for index in range(len(startWord)):
        for i in range(26):
            newWord=startWord[:index]+chr(ord("a")+i)+startWord[index+1:]
            if newWord==startWord:
                continue
            elif newWord==endWord:
                return path+[endWord]               
            elif newWord in wordDic and newWord not in visited:
                visited.add(newWord)
                res=wordLadder(newWord, endWord, wordDic, path+[newWord],visited)
                if res:
                    return res
                visited.remove(newWord)
    return None
def wordLadder2(startWord,endWord,wordDic,path,visited,res):
    for index in range(len(startWord)):
        for i in range(26):
            newWord=startWord[:index]+chr(ord("a")+i)+startWord[index+1:]
            if newWord==startWord:
                continue
            elif newWord==endWord:
                res.append(path+[endWord])               
            elif newWord in wordDic and newWord not in visited:
                visited.add(newWord)
                wordLadder2(newWord, endWord, wordDic, path+[newWord],visited,res)
                visited.remove(newWord)
startWord="hit"
endWord="cog"
wordDic=["hot","dot","dog","lot","log"]
print("->".join(wordLadder(startWord, endWord, wordDic, ["hit"],set())))
res=[]
wordLadder2(startWord, endWord, wordDic, [startWord], set(), res)
print(res)
for item in res:
    print("->".join(item))