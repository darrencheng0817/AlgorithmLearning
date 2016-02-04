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
    graph = {}
    inDegree = {}
    for wordsIndex in range(len(words)):
        for char in words[wordsIndex]:
            if char not in graph:
                graph[char] = set()
            if char not in inDegree:
                inDegree[char] = 0
        if wordsIndex > 0:
            charIndex = 0
            while charIndex < len(words[wordsIndex]) and charIndex < len(words[wordsIndex - 1]) and words[wordsIndex][charIndex] == words[wordsIndex - 1][charIndex]:
                charIndex += 1
            if charIndex < len(words[wordsIndex]) and charIndex < len(words[wordsIndex - 1]) and words[wordsIndex][charIndex] != words[wordsIndex - 1][charIndex]:
                graph[words[wordsIndex - 1][charIndex]].add(words[wordsIndex][charIndex])
                inDegree[words[wordsIndex][charIndex]] += 1
    print(graph)
    queue = []
    visited = set()
    for key, value in inDegree.items():
        if value == 0:
            queue.append(key)
    res = ""
    while queue:
        char = queue.pop(0)
        if char in visited:
            return ""
        else:
            res += char
            for tempChar in graph[char]:
                queue.append(tempChar)
            visited.add(char)
    
    return res if len(visited) == len(inDegree) else ""
 
words = ["wrt", "wrf", "er", "ett", "rftt"]  
words=["za","zb","ca","cb"]     
print(alineDictionary(words)) 


