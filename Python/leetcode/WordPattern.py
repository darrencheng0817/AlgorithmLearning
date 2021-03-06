'''
Created on 1.12.2016

@author: Darren
''''''
Given a pattern and a string str, find if str follows the same pattern.
 Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
Credits:Special thanks to @minglotus6 for adding this problem and creating all test cases." 
'''

def wordPattern(pattern, string):
    s = pattern
    t = string.split()
    return list(map(s.find, s)) == list(map(t.index, t))

pattern = "abab"
string = "red blue red blue"
print(wordPattern(pattern, string))
