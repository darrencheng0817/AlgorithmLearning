'''
Created on 2016年3月1日

@author: Darren
'''
import unittest

def getNearestPalindrome(num):
    if len(str(num))!=4:
        raise Exception("")
    digits=list(str(num))
    candidate=int("".join(digits[:2]+digits[:2][::-1]))
    count=1
    while count<abs(num-candidate):
        new_candidate1=num+count
        if str(new_candidate1)==str(new_candidate1)[::-1]:
            return new_candidate1
        new_candidate2=num-count
        if str(new_candidate2)==str(new_candidate2)[::-1]:
            return new_candidate2
        count+=1
    return candidate
            
def getNearestPalindrome2(num):
    numString=str(num)
    mid="" if len(numString)&1==0 else numString[len(numString)//2]
    firstHalf=numString[:len(numString)//2]
    candidate1=int(firstHalf+mid+firstHalf[::-1])
    candidateDigitList=list(str(candidate1))
    idx = (len(candidateDigitList)-1)//2
    if candidate1>num:
        while idx>=0:
            if candidateDigitList[idx]=="0":
                candidateDigitList[idx]="9"
                idx-=1
            else:
                candidateDigitList[idx]=str(int(candidateDigitList[idx])-1)
                break
    else:
        while idx>=0:
            if candidateDigitList[idx]=="9":
                candidateDigitList[idx]="0"
                idx-=1
            else:
                candidateDigitList[idx]=str(int(candidateDigitList[idx])+1)
                break
    mid="" if len(candidateDigitList)&1==0 else candidateDigitList[len(candidateDigitList)//2]
    firstHalf="".join(candidateDigitList[:len(candidateDigitList)//2])
    candidate2=int(firstHalf+mid+firstHalf[::-1])
    return min(candidate1,candidate2,key=lambda x:abs(x-num))
            

class Test(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
    
    def test_getNearestPalindrome(self):
        testCases=[1999,1234]
        expectResults=[2002,1221]
        for index,testCase in enumerate(testCases):
            actualResult=getNearestPalindrome(testCase)
            self.assertEqual(expectResults[index], actualResult)
    
    def test_test_getNearestpalindrome2(self):
        testCases=[1999,1234,19999,900000]
        expectResults=[2002,1221,20002,899998]
        for index,testCase in enumerate(testCases):
            actualResult=getNearestPalindrome2(testCase)
            self.assertEqual(expectResults[index], actualResult)
            
unittest.main()