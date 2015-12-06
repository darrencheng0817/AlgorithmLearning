from timeit import Timer
mem={}
def nimGame(n):
    if n<=3 and n>0:
        return True
    if n not in mem:
        mem[n]=False
        if not nimGame(n-1):
            mem[n]= True
        elif not nimGame(n-2):
            mem[n]= True
        elif not nimGame(n-3):
            mem[n]= True
    return mem[n]
    
def nimGame2(n):
    if n<=3 and n>0:
        return True
    if not nimGame(n-1):
        return True
    elif not nimGame(n-2):
        return True
    elif not nimGame(n-3):
        return True
    return False

    
n=1000
def mytest1():
    nimGame(n)
def mytest2():
    nimGame2(n)
print(nimGame(n))
print(nimGame2(n))
t1=Timer('mytest1()', 'from __main__ import mytest1')
t2=Timer('mytest2()', 'from __main__ import mytest2')

print(t1.timeit(100))
print(t2.timeit(100))