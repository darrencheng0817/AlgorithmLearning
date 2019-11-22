'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(1, n)

    def helper(self, l, u):
        print(l, u)
        if l > u:
            return 1
        if l == u:
            return 1
        res = 0
        for i in range(l, u + 1):
            res += self.helper(l, i-1) * self.helper(i + 1, u)
        return res

s = Solution()
print(s.numTrees(3))