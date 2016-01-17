'''
Created on 2016年1月16日

@author: Darren
'''
# smallest time difference
def timeToMinutes(timeString):
    timeString=timeString.strip().split(":")
    hour=int(timeString[0])
    minute=int(timeString[1])
    return hour*60+minute
def  getMinTimeDifference(times):
    timeList=[]
    for eachTime in times:
        timeList.append(timeToMinutes(eachTime))
    timeList=sorted(timeList)
    res=timeList[-1]
    for index in range(1,len(timeList)):
        res=min(res,timeList[index]-timeList[index-1])
    res=min(res,timeList[0]+24*60-timeList[-1])#for the smallest and the largest
    return res