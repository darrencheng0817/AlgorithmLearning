'''
Created on 2015年12月1日
1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result.
@author: Darren
'''
def applyOp(op,num1,num2):
    if op=="+":
        return num1+num2
    if op=="-":
        return num2-num1
    if op=="*":
        return num1*num2
    if op=="/":
        return num2//num1

def hasPrecedence(op1,op2):
    if op1=="(" or op1==")":
        return False
    if op2 in ["*","/"] and op1 in ["+","-"]:
        return False
    return True


def evaluate(string):
    if not string:
        return 0
    index=0
    valueStack=[]
    operationStack=[]
    while index<len(string):
        char=string[index]
        if char==" ":
            index+=1
            continue
        if char.isdigit():
            startIndex=index
            while index<len(string) and string[index].isdigit():
                index+=1
            valueStack.append(int(string[startIndex:index]))
        elif char=="(":
            operationStack.append(char)
            index+=1
        elif char==")":
            while operationStack[-1]!="(":
                valueStack.append(applyOp(operationStack.pop(),valueStack.pop(),valueStack.pop()))
            operationStack.pop()
            index+=1
        elif char in ["+","-","*","/"]:
            while operationStack and hasPrecedence(operationStack[-1],char):
                valueStack.append(applyOp(operationStack.pop(),valueStack.pop(),valueStack.pop()))
            operationStack.append(char)
            index+=1
    while operationStack:
        valueStack.append(applyOp(operationStack.pop(),valueStack.pop(),valueStack.pop()))
    return valueStack.pop()
print(evaluate("0- (3+4)*6/2"))