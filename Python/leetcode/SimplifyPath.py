'''
Created on 1.12.2016

@author: Darren
'''
'''
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.
Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes  /  together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return "/"
        stack=[]
        path_list=path.split("/")
        for item in path_list:
            if item and item not in [".",".."]:
                stack.append(item)
            elif item==".." and stack:
                stack.pop()
        if not stack:
            return "/"
        return "/"+"/".join(stack)
