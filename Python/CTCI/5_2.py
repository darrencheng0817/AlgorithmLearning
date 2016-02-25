'''
Created on 2016年2月24日

@author: Darren
'''
'''
Given a real number between 0 and 1(e.g.,0.72)that is passed in as a double,
print the binary representation. If the number cannot be represented accurately 
in binary with at most 32 characters, print "ERROR."
'''
def num_2_binary(num):
    if not 0<num<1:
        return "Error"
    res="0."
    while True:
        num*=2
        if num==1:
            res+="1"
            return res
        elif num>1:
            num-=1
            res+="1"
        else:
            res+="0"
        if len(res)>32:
            return "Error"
    
print(num_2_binary(0.125))
print(bin(3)[2:])