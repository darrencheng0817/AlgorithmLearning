'''
Created on 2016年2月23日

@author: Darren
'''
'''
Given an image represented by an NxN matrix, 
where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
Can you do this in place?
'''
'''
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/


/*
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
'''

def rotate(matrix):
    matrix=matrix[::-1]
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix

def rotate2(A):
    n = len(A)
    for i in range(n//2):
        for j in range(n-n//2):
            A[i][j], A[n-1-j][i], A[n-1-i][n-1-j], A[j][n-1-i] = \
                     A[n-1-j][i], A[n-1-i][n-1-j], A[j][n-1-i], A[i][j]
    return A                
matrix=[[1,2,3],[4,5,6],[7,8,9]]

print(rotate(matrix))
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate2(matrix))