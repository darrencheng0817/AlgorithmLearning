'''
Created on 2016年1月26日

@author: Darren
'''
def convertPreToPost(preOrder):
    if not preOrder:
        return []
    index=1
    while index<len(preOrder) and preOrder[index]<preOrder[0]:
        index+=1
    return convertPreToPost(preOrder[1:index])+convertPreToPost(preOrder[index:])+[preOrder[0]]
     

preOrder=[]
while True:
    try:
        preOrder.append(int(input()))
    except EOFError:
        break
postOrder=convertPreToPost(preOrder)
print(" ".join([str(_) for _ in postOrder]))