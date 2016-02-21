'''
Created on 1.12.2016

@author: Darren
''''''

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ). 



Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]



Credits:Special thanks to @hpplayer for adding this problem and creating all test cases." 
'''
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def check(s):
            if not s:
                return False
            count=0
            for char in s:
                if char=="(":
                    count+=1
                elif char ==")":
                    count-=1
                if count<0:
                    return False
            return count==0
        queue=[s]
        res=[]
        visited=set()
        while queue:
            new_queue=[]
            while queue:
                string=queue.pop()
                if check(string):
                    res.append(string)
                for index,char in enumerate(string):
                    if char in ["(",")"]:
                        new_string=string[:index]+string[index+1:]
                        if new_string in visited:
                            continue
                        new_queue.append(new_string)
                        visited.add(new_string)
            if res:
                return res
            queue=new_queue
        return [""]    
                 
so=Solution()
s="()()()((())n"
print(so.removeInvalidParentheses(s))