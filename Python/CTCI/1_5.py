'''
Created on 2016年2月23日

@author: Darren
'''
'''
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string aabcccccaaa would become a2blc5a3. 
If the "compressed" string would not become smaller than the orig- inal string, 
your method should return the original string.
'''
def compress(string):
    if not string:
        return string
    pre,count=string[0],0
    res=""
    for char in string:
        if char==pre:
            count+=1
        else:
            res+=pre+str(count)
            pre=char
            count=1
    res+=pre+str(count)
    if len(res)>=len(string):
        return string
    return res

string="aabcccccaaa"
print(compress(string))