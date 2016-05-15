'''
Created on 2016年5月14日

@author: Darren
'''
'''
Consider the number triangle shown below. Write a program that calculates the highest sum of numbers that can be passed on a route that starts at the top and ends somewhere on the base. Each step can go either diagonally down to the left or diagonally down to the right.

          7

        3   8

      8   1   0

    2   7   4   4

  4   5   2   6   5
In the sample above, the route from 7 to 3 to 8 to 7 to 5 produces the highest sum: 30.

PROGRAM NAME: numtri

INPUT FORMAT

The first line contains R (1 <= R <= 1000), the number of rows. Each subsequent line contains the integers for that particular row of the triangle. All the supplied integers are non-negative and no larger than 100.
SAMPLE INPUT (file numtri.in)

5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
OUTPUT FORMAT

A single line containing the largest sum using the traversal specified.
SAMPLE OUTPUT (file numtri.out)

30
'''

def load_data(file_name):
    file = open(file_name,"r",newline="\n")
    N=int(file.readline())
    data=[]
    for i in range(N):
        line=file.readline()
        line=line.strip().split(" ")
        line=list(map(int,line))
        data.append(line)
    return data

def numbri():
    data=load_data("numbri.in")
    for i in range(len(data)-2,-1,-1):
        for j in range(len(data[i])):
            data[i][j]+=max(data[i+1][j],data[i+1][j+1])
    return data[0][0]
        
print(numbri())


