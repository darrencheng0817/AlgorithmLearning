'''
Created on 2015年12月1日
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
https://leetcode.com/problems/basic-calculator/
@author: Darren
'''
def calculate(string):
    if not string:
        return 0
    sign,res,num=1,0,0
    resStack=[]
    for char in string:
        if char.isdigit():
            num=num*10+int(char)
        elif char=="+":
            res+=num*sign
            num=0
            sign=1
        elif char=="-":
            res+=num*sign
            num=0
            sign=-1
        elif char=="(":
            resStack.append(res)
            resStack.append(sign)
            res=0
            sign=1
        elif char==")":
            res+=num*sign
            res*=resStack.pop()
            res+=resStack.pop()
            num=0
            sign=1
    if num!=0:
        res+=num*sign
    return res

print(calculate("(1+(4+5+2)-3)+(6+83)"))