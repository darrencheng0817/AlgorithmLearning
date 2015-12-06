'''
Created on 2015年12月6日

@author: Darren
'''

i=81
while i>0:
    if i//9%3==i%9%3:
        i-=1
        continue
    print(i//9+1,i%9+1)
    i-=1