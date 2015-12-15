'''
Created on 2015年12月1日

@author: Darren
'''


global count
count=0
def solve(nums,target):
    expression=[str(num) for num in nums]
    if solveUtil(nums,target,expression,len(nums)):
        print(expression[0])
    else:
        print("No result!")
def solveUtil(nums,target,expression,n):
    print(nums)
    global count
    count+=1
    if n==1:
        if nums[0]==target:
            return True
        else:
            return False
    for i in range(n):
        for j in range(i+1,n):
            a,b=nums[i],nums[j]
            expa,expb=expression[i],expression[j]
            nums[j]=nums[n-1]
            expression[j]=expression[n-1]
            
            expression[i]='('+expa+'+'+expb+')'
            nums[i]=a+b
            if solveUtil(nums, target,expression,n-1):
                return True  
              
            expression[i]='('+expa+'-'+expb+')'
            nums[i]=a-b
            if solveUtil(nums, target,expression,n-1):
                return True  
             
            expression[i]='('+expb+'-'+expa+')'
            nums[i]=b-a
            if solveUtil(nums, target,expression,n-1):
                return True  
             
            expression[i]='('+expa+'*'+expb+')'
            nums[i]=a*b
            if solveUtil(nums, target,expression,n-1):
                return True   
            
            if b!=0 and a%b==0:
                expression[i]='('+expa+'//'+expb+')'
                nums[i]=a//b
                if solveUtil(nums, target,expression,n-1):
                    return True  
            if a!=0 and b%a==0:
                expression[i]='('+expb+'//'+expa+')'
                nums[i]=b//a
                if solveUtil(nums, target,expression,n-1):
                    return True  
            nums[i],nums[j]=a,b
            expression[i],expression[j]=expa,expb
        return False


solve([9,3,8,1], 22)
print(count)