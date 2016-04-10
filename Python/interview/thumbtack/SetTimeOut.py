'''
Created on 2016年3月1日

@author: Darren
'''


import time
from _heapq import heapify, heappush, heappop
class SetTimeOut():
    def __init__(self):
        self.requests={}
        self.call_times=[]
        heapify(self.call_times)
        
    def setTimeOut(self,callBackFunc,delayDuration):
        current_time=int(round(time.time() * 1000))
        call_time=current_time+delayDuration
        if call_time not in self.requests:
            self.requests[call_time]=[]
        self.requests[call_time].append(callBackFunc)
        heappush(self.call_times,call_time)
        
        
    def check(self):
        if not self.call_times:
            return
        current_time=int(round(time.time() * 1000))
        while self.call_times and self.call_times[0]<=current_time:
            call_time=heappop(self.call_times)
            for func in self.requests[call_time]:
                func()
            self.requests.pop(call_time)
        
        

def myPrint():
    print("OK")

def test():
    setTimeOut=SetTimeOut()
    setTimeOut.setTimeOut(myPrint, 3000)
    time.sleep(1)
    setTimeOut.check()
    time.sleep(4)
    setTimeOut.check()
    
test()