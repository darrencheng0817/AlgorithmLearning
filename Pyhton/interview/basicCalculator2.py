'''
Created on 2015年12月1日
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
https://leetcode.com/problems/basic-calculator-ii/
@author: Darren
'''

def calculate(string):
    if not string:
        return 0
    res, num = 0, 0
    resStack = []
    sign = "+"
    index = 0
    while index < len(string):
        if string[index] in ["+", "-", "/", "*"]:
            sign = string[index]
            index += 1
        tempIndex = index
        while index < len(string) and (string[index].isdigit()or string[index] == " "):
            index += 1
        num = int(string[tempIndex:index].strip())
        if sign == "+":
            resStack.append(num)
        elif sign == "-":
            resStack.append(-num)
        elif sign == "*":
            tempNum = resStack.pop()
            resStack.append(tempNum * num)
        elif sign == "/":
            temNum = resStack.pop()
            resStack.append(tempNum / num)
    for num in resStack:
        res += num
    return res

print(calculate("0- 20+89"))
