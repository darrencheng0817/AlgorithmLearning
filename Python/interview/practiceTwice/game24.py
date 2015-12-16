'''
Created on 2015年12月1日

@author: Darren
'''


def solve(nums,target):
    expression=[str(__temp) for __temp in nums]
    if solveUtil(nums, target, expression, len(nums)):
        return expression[0]
    else:
        return "No result found!"

def solveUtil(nums,target,expression,index):
    if index==1:
        if nums[0]==target:
            return True
        else:
            return False
    for i in range(index):
        for j in range(i+1,index):
            a,b=nums[i],nums[j]
            expa,expb=expression[i],expression[j]
            nums[j]=nums[index-1]
            expression[j]=expression[index-1]
            
            nums[i]=a+b
            expression[i]="("+expa+"+"+expb+")"
            if solveUtil(nums, target, expression, index-1):
                return True
            
            nums[i]=a-b
            expression[i]="("+expa+"-"+expb+")"
            if solveUtil(nums, target, expression, index-1):
                return True
            
            nums[i]=b-a
            expression[i]="("+expb+"-"+expa+")"
            if solveUtil(nums, target, expression, index-1):
                return True
                      
            nums[i]=a*b
            expression[i]="("+expa+"*"+expb+")"
            if solveUtil(nums, target, expression, index-1):
                return True   
              
            if b!=0 and a%b==0:
                nums[i]=a//b
                expression[i]="("+expa+"/"+expb+")"
                if solveUtil(nums, target, expression, index-1):
                    return True  
             
            if a!=0 and b%a==0:       
                nums[i]=b//a
                expression[i]="("+expb+"+"+expa+")"
                if solveUtil(nums, target, expression, index-1):
                    return True    
            
            nums[i],nums[j]=a,b   
            expression[i],expression[j]=expa,expb
    return False        

def getCand(nums):
    return [[num]+temp for i,num in enumerate(nums) for temp in getCand(nums[:i]+nums[i+1:])] or [[]]

def solve2Util(cand,target,index,res,item,curValue,multed):
    if index==len(cand):
        if curValue==target:
            res.append(item)
            return True
        return False
    if solve2Util(cand, target, index+1, res, item+"+"+str(cand[index]), curValue+cand[index], cand[index]):
        return True
    if solve2Util(cand, target, index+1, res, item+"-"+str(cand[index]), curValue-cand[index], -cand[index]):
        return True
    if solve2Util(cand, target, index+1, res, item+"*"+str(cand[index]), curValue-multed+multed*cand[index], multed*cand[index]):
        return True
    if cand[index]!=0 and multed%cand[index]==0 and solve2Util(cand, target, index+1, res, item+"/"+str(cand[index]), curValue-multed+multed//cand[index], multed//cand[index]):
        return True
    return False

def solve2(nums,target):
    cands=getCand(nums)
    res=[]
    for cand in cands:
        if solve2Util(cand,target,1,res,str(cand[0]),cand[0],cand[0]):
            return res[0]
    return "No result found!"
        
print(solve([6,6,2,1], 24))
print(solve2([6,6,2,1], 24))