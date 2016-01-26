'''
Created on 1.12.2016

@author: Darren
''''''
LeetCode Online Judge is a platform for preparing technical coding interviews and assessing your knowledge of data structures and algorithms. Pick from our expanding library of more than 160 interview questions to solve. Use our automated tool to get real time feedback on your solution." 
'''

def alineDictionary(words):
    graph = {}
    inDegree = {}
    for wordsIndex in range(len(words)):
        for char in words[wordsIndex]:
            if char not in graph:
                graph[char] = []
            if char not in inDegree:
                inDegree[char] = 0
        if wordsIndex > 0:
            charIndex = 0
            while charIndex < len(words[wordsIndex]) and charIndex < len(words[wordsIndex - 1]) and words[wordsIndex][charIndex] == words[wordsIndex - 1][charIndex]:
                charIndex += 1
            if charIndex < len(words[wordsIndex]) and charIndex < len(words[wordsIndex - 1]) and words[wordsIndex][charIndex] != words[wordsIndex - 1][charIndex]:
                graph[words[wordsIndex - 1][charIndex]].append(words[wordsIndex][charIndex])
                inDegree[words[wordsIndex][charIndex]] += 1
    
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
print(alineDictionary(words)) 