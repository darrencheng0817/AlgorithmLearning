'''
Created on 2016年2月9日

@author: Darren
'''
'''
Transformations
A square pattern of size N x N (1 <= N <= 10) black and white square tiles is transformed into another square pattern. Write a program that will recognize the minimum transformation that has been applied to the original pattern given the following list of possible transformations:

#1: 90 Degree Rotation: The pattern was rotated clockwise 90 degrees.
#2: 180 Degree Rotation: The pattern was rotated clockwise 180 degrees.
#3: 270 Degree Rotation: The pattern was rotated clockwise 270 degrees.
#4: Reflection: The pattern was reflected horizontally (turned into a mirror image of itself by reflecting around a vertical line in the middle of the image).
#5: Combination: The pattern was reflected horizontally and then subjected to one of the rotations (#1-#3).
#6: No Change: The original pattern was not changed.
#7: Invalid Transformation: The new pattern was not obtained by any of the above methods.
In the case that more than one transform could have been used, choose the one with the minimum number above.

PROGRAM NAME: transform

INPUT FORMAT

Line 1:    A single integer, N
Line 2..N+1:    N lines of N characters (each either `@' or `-'); this is the square before transformation
Line N+2..2*N+1:    N lines of N characters (each either `@' or `-'); this is the square after transformation
SAMPLE INPUT (file transform.in)

3
@-@
---
@@-
@-@
@--
--@
OUTPUT FORMAT

A single line containing the the number from 1 through 7 (described above) that categorizes the transformation required to change from the `before' representation to the `after' representation.
SAMPLE OUTPUT (file transform.out)

1
'''
def get_input():
    file=open("transform.in","r")
    N=int(file.readline().strip())
    origin=[]
    for _index in range(N):
        line=list(file.readline().strip())
        origin.append(line)
    transformed=[]
    for _index in range(N):
        line=list(file.readline().strip())
        transformed.append(line)
    return origin,transformed

def compare(A,B):
    for row in range(len(A)):
        for col in range(len(A[0])):
            if A[row][col]!=B[row][col]:
                return False
    return True

def rotate90(A):
    l=len(A)
    res=[[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            res[j][l-i-1]=A[i][j]
    return [res]

def rotate180(A):
    l=len(A)
    res=[[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            res[l-i-1][l-j-1]=A[i][j]
    return [res]

def rotate270(A):
    l=len(A)
    res=[[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            res[l-j-1][i]=A[i][j]
    return [res]

def reflect(A):
    l=len(A)
    res=[[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            res[i][l-j-1]=A[i][j]
    return [res]

def combination(A):
    A=reflect(A)[0]
    res=[]
    funcs=[rotate90,rotate180,rotate270]
    for func in funcs:
        res.append(func[func(A)])
    return res


def solution():
    origin,transformed=get_input()
    check_funcs=[rotate90,rotate180,rotate270,reflect,combination]
    for index,func in enumerate(check_funcs):
        trans=func(origin)
        for tran in trans:
            if compare(transformed,tran):
                return index+1
    if compare(transformed,origin):
        return 6
    return 7
    
print(solution())
