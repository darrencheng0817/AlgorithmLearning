'''
Created on 2016年1月16日

@author: Darren
'''
# find fraud
def  getSuspiciousList( transactions):
    if not transactions or len(transactions)<=0:
        return []
    cache={}
    midRes,fraudName={},set()
    for transaction in transactions:
#        print(transaction)
        infoList=transaction.strip().split("|")
        name=infoList[0]
        amount=int(infoList[1])
        location=infoList[2]
        transactionTime=int(infoList[3])
        if name in fraudName:
            break      
        if amount>3000:
            fraudName.add(name)
            midRes[transactionTime]=name
        elif name in cache:
            lastLocation,lastTime=cache[name]
            if lastLocation!=location and transactionTime-lastTime<60:
                fraudName.add(name)
                midRes[lastTime]=name
        cache[name]=(location,transactionTime)
    res=[]
    for key in sorted(midRes.keys()):
        res.append(midRes[key])
    return res