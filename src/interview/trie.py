'''
Created on 2015年12月1日
implementation of trie
@author: Darren
'''
from models.Trie import TrieNode

class Trie(object):
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,string):
        if not string:
            return
        pointer=self.root
        for char in string:
            if char not in pointer.children:
                pointer.children[char]=TrieNode()
            pointer=pointer.children[char]
        pointer.isword=True
        
    def searchUtil(self,string):
        if not string:
            return None
        pointer=self.root
        for char in string:
            if char not in pointer.children:
                return None
            pointer=pointer.children[char]
        return pointer
    
    def find(self,string):
        pointer=self.searchUtil(string)
        if pointer==None or pointer.isword==False:
            return False
        return True
    
    def startWith(self,string):
        pointer=self.searchUtil(string)
        return not pointer==None

trie=Trie()
trie.insert("abcdefg")
print(trie.find("abcdefg"))
print(trie.find("abcddefg"))
print(trie.startWith("abcd"))