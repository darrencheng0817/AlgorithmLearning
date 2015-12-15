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

def applyOp(op,a,b):
    '''
    // A utility method to apply an operator 'op' on operands 'a' 
    // and 'b'. Return the result.
    '''
    if op=="+":
        return a+b
    elif op=="-":
        return b-a
    elif op=="*":
        return a*b
    elif op=="/":
        return b//a
def hasPrecedence(op1,op2):
    '''
    // Returns true if 'op2' has higher or same precedence as 'op1',
    // otherwise returns false.
    '''
    if op2=="(" or op2==")":
        return False
    if (op1=="*" or op1=="/") and (op2=="+" or op2=="-"):
        return False
    else:
        return True
    
def evaluate(string):
    values=[]
    ops=[]
    index=0
    while index<len(string):
        if string[index]==" ":
            index+=1
            continue
        if string[index].isdigit():
            start=index
            while index<len(string) and string[index].isdigit():
                index+=1
            values.append(int(string[start:index]))
        elif string[index]=="(":
            ops.append(string[index])
            index+=1
        elif string[index]==")":
            while ops[-1]!="(":
                values.append(applyOp(ops.pop(),values.pop(),values.pop()))
            ops.pop()
            index+=1
        elif string[index] in ["+","-","*","/"]:
            while ops and hasPrecedence(string[index],ops[-1]):
                values.append(applyOp(ops.pop(),values.pop(),values.pop()))
            ops.append(string[index])
            index+=1
    while ops:
        values.append(applyOp(ops.pop(),values.pop(),values.pop()))
    return values.pop()

def simpleCal(string):
    if not string:
        return 0
    index=0
    numStack=[]
    signStack=[]
    while index<len(string):
        char=string[index]
        if char.isdigit():
            startIndex=index
            while index<len(string) and string[index].isdigit():
                index+=1
            num=int(string[startIndex:index])
            numStack.append(num)
        elif char in ["+","-","*","/"]:
            while signStack and hasPrecedence(char, signStack[-1]):
                numStack.append(applyOp(signStack.pop(), numStack.pop(), numStack.pop()))
            signStack.append(char)
            index+=1
        else:
            index+=1
    while signStack:
        numStack.append(applyOp(signStack.pop(), numStack.pop(), numStack.pop()))
    return numStack.pop()
print(evaluate("0- (3+4)*6/2"))
print(simpleCal("4+5*6+3"))