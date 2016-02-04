'''
Created on 2016年2月3日

@author: Darren
'''
'''
input:"abc"
return:['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC']
'''
def solution(string):
    res=[]
    util(res,0,string,"")
    return res
    
def util(res,index,string,item):
    if index==len(string):
        res.append(item)
        return
    util(res,index+1,string,item+string[index])
    if string[index].isupper():
        util(res,index+1,string,item+string[index].lower())
    elif string[index].islower():
        util(res,index+1,string,item+string[index].upper())

def solution2(string):
    res=[string]
    for index in range(len(string)):
        newList=[]
        for item in res:
            newString=""
            if item[index].isupper():
                newString=item[:index]+item[index].lower()+item[index+1:]
            elif item[index].lower():
                newString=item[:index]+item[index].upper()+item[index+1:]
            else:
                continue
            newList.append(newString) 
        res.extend(newList)
    return res        
    
print(solution("abc"))
print(solution2("abc"))