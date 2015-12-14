'''
Created on 2015年12月1日
https://leetcode.com/problems/alien-dictionary/
Given the following words in dictionary,
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".
@author: Darren
'''

def alineDictionary(words):
    if not words:
        return ""
    graph={}
    indegree={}
    for wordIndex,word in enumerate(words):
        for char in word:
            if char not in graph:
                graph[char]=[]
            if char not in indegree:
                indegree[char]=0
        if wordIndex>0:
            i,j=0,0
            while i<len(words[wordIndex-1]) and j<len(words[wordIndex]) and words[wordIndex-1][i]==words[wordIndex][j]:
                i+=1
                j+=1
            if i<len(words[wordIndex-1]) and j<len(words[wordIndex]) and words[wordIndex-1][i]!=words[wordIndex][j]:
                graph[words[wordIndex-1][i]]=words[wordIndex][j]
                indegree[words[wordIndex][j]]+=1
    queue=[char for char in indegree if indegree[char]==0]
    visited=set()
    res=""
    while queue:
        char =queue.pop(0)
        if char in visited:
            return ""
        visited.add(char)
        res+=char
        queue+=graph[char]
        
    return res if len(visited)==len(indegree) else ""
    
words = ["wrt", "wrf", "er", "ett", "rftt"]       
print(alineDictionary(words)) 

