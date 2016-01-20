'''
Created on 2016年1月18日

@author: Darren
'''
# Complete the function below.
from math import ceil,floor

def  rpn_calculate(tokens):
    if not tokens or len(tokens)<1:
        print("Invalid input")
        return
    stack=[]
    for token in tokens:
        if token.isdigit(): # isdigit() will return False for negative number like "-1"
            stack.append(int(token))
        elif len(token)>1 and token[0]=="-" and token[1:].isdigit():# for the negative number
            stack.append(-1*int(token))
        elif token in ["-","+","*","/"]:
            if not stack or len(stack)<2:
                print("Invalid input")
                return
            num2=stack.pop()
            num1=stack.pop()
            if token=="-":
                stack.append(num1-num2)
            elif token=="+":
                stack.append(num1+num2)
            elif token=="*":
                stack.append(num1*num2)
            else:
                if num2==0:
                    print("Invalid input")
                    return
                if num1==0:
                    stack.append(0)
                elif num1*num2<0:
                    stack.append((abs(num1)//abs(num2))*-1) # in python -3//-5 is -1 so need to be handled 
                else:
                    stack.append(num1//num2)
        else:
            print("Invalid input")
            return
    if not stack or len(stack)!=1:
        print("Invalid input")
    else:
        print(stack.pop())
            

            


tokens=["-3","5","/"]
rpn_calculate(tokens)
s=set([1,2,3])
print(floor(-4.6))