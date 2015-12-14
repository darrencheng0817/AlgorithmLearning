'''
Created on 2015年12月1日
implementation of trie
@author: Darren
'''
from models.Trie import TrieNode

class Trie(object):
    pass

trie=Trie()
trie.insert("abcdefg")
print(trie.find("abcdefg"))
print(trie.find("abcddefg"))
print(trie.startWith("abcd"))