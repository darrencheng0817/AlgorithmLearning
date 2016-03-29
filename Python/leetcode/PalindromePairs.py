'''
Created on 2016年3月28日

@author: Darren
'''
'''
Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''
'''
Sort all words and all reversed words. One word (call it A) is the prefix of the following words (call it B). 
If A is B's prefix and one is reversed one is not, and their indexes are different, 
then we find a palindrome pair.
'''
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 0 means the word is not reversed, 1 means the word is reversed
        words= sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
                                       [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)])
        length, result = len(words), []
        for i, (word1, rev1, ind1, len1) in enumerate(words):
            for j in range(i + 1, length):
                word2, rev2, ind2, _ = words[j]
                if word2.startswith(word1):
                    if ind1 != ind2 and rev1 ^ rev2:
                        rest = word2[len1:]
                        if rest == rest[::-1]: 
                            result += ([ind1, ind2],) if rev2 else ([ind2, ind1],)
                else:
                    break
        return result

            
            
            
so=Solution()
words = ["abcd", "dcba", "lls", "s", "sssll"]
print(so.palindromePairs(words))
            