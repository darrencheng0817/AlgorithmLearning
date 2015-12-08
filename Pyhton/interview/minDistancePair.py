'''
Created on 2015年12月1日
给一个整数n，输出俩数x和y，使得x*y的值在 [n, n+2] 的范围内，同时保证 |x - y|  最小
从x=y=sqrt(n+2) 开始搜索，第一次碰到一对x和y，能满足[n,  n+2], 那这对x y就是要返回的结果
int[] searchXandY(int n) {
                int[] result = new int[2];
                if(n <= 0) {
                        throw new IllegalArgumentException("Illegal input");.
                }
                
                int cand1 = (int)Math.sqrt(n+2);
                int cand2 = (int)Math.sqrt(n+2);
                
                while(true) {
                        
                        if(cand1 * cand2 >= n && cand1 * cand2 <= n +2) {
                                result[0] = cand1;
                                result[1] = cand2;
                                break;
                        } else if(cand1 * cand2 < n) {
                                cand1++;
                        } else {
                                cand2--;
                        }
                }
                return result;
        }
@author: Darren
'''
from math import sqrt
def findMinDistancePair(num):
    cand1=int(sqrt(num+2))
    cand2=int(sqrt(num+2))
    while True:
        if cand1*cand2>=num and cand1*cand2<=num+2:
            return (cand1,cand2)
        elif cand1*cand2<num:
            cand1+=1
        else:
            cand2-=1

print(findMinDistancePair(25))
nums=[25,24,21,23,20]
for num in nums:
    print(findMinDistancePair(num))