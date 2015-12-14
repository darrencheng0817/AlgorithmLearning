'''
Created on 2015.11.30

We obtained a log file containing runtime information about all threads and mutex locks of a user program.
The log file contains N lines of triplets about threads acquiring or releasing mutex locks.
The format of the file is: The first line contains an integer N indicating how many more lines are in the file.
Each of the following N lines contains 3 numbers separated by space. The first number is an integer 
representing thread_id (starting from 1). The second number is either 0 (acquiring) or 1 (releasing). 
The third number is an integer representing mutex_id (starting from 1). Now we want you to write a detector 
program that reads the logs line by line and output the line number of the trace where a deadlock happens. 
If there is no deadlock after reading all log traces, output 0.

Example:
4
1 0 1
2 0 2
2 0 1
1 0 2

Output:
4

Example:
3
1 0 3
2 0 1
3 0 2
Output:
3
@author: Darren
'''


def detector():
    pass
print(detector())
