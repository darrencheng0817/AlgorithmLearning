'''
Created on 2015年12月4日
given [1, [2,3], [[4]]], return sum. 计算sum的方法是每向下一个level权重+1， 
例子的sum = 1 * 1 + (2 + 3) * 2 + 4 * 3。follow up：每向下一个level 权重 - 1， sum = 3 * 1 +（2 + 3）* 2 + 4 * 1 
@author: Darren
'''


def levelSum(string):
    if not string:
        return 0
    index=0
    level=0
    maxLevel=0
    d={}
    while index<len(string):
        char= string[index]
        if char=="[":
            level+=1
            maxLevel=max(maxLevel,level)
            index+=1
        elif char.isdigit():
            startIndex=index
            while string[index].isdigit():
                index+=1
            num=int(string[startIndex:index])
            if level not in d:
                d[level]=[]
            d[level].append(num)
        elif char=="]":
            level-=1
            index+=1
        else:
            index+=1
    res=0
    for key,value in d.items():
        for num in value:
            res+=(maxLevel-key+1)*num
    return res
    
print(levelSum("[1, [2,3], [2,3],[[4]]]") )