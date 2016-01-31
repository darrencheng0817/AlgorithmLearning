'''
Created on 2016年1月30日
Unfinished
@author: Darren
'''
'''
Alice thinks of a non-decreasing sequence of non-negative integers and wants Bob to guess it by providing him the set of all its K-sums with repetitions.

What is this? Let the sequence be {A[1], A[2], ..., A[N]} and K be some positive integer that both Alice and Bob know. Alice gives Bob the set of all possible values that can be genereated by this - A[i1] + A[i2] + ... + A[iK], where 1 ≤ i1 ≤ i2 ≤ ... ≤ iK ≤ N. She can provide the values generated in any order she wishes to. Bob's task is to restore the initial sequence.

Consider an example. Let N = 3 and K = 2. The sequence is {A[1], A[2], A[3]}. The sequence of its 2-sums with repetitions is {A[1] + A[1], A[1] + A[2], A[1] + A[3], A[2] + A[2], A[2] + A[3], A[3] + A[3]}. But its elements could be provided in any order. For example any permutation of {2, 3, 4, 4, 5, 6} corresponds to the sequence {1, 2, 3}.

Input Format 
The first line of the input contains an integer T denoting the number of test cases. 
The description of T test cases follows. 
The first line of each test case contains two space separated integers N and K. 
The second line contains the sequence Si of all K-sums with repetitions of the sequence Alice initially thought of.

Output Format 
For each test case, output a single line containing the space separated list of elements of the non-decreasing sequence Alice thinks of. If there are several possible outputs you can output any of them.

Constraints 
1 <= T <= 105 
1 <= N <= 105 
1 <= K <= 109 
2 <= Si <= 1018

Note 
The total number of elements in any input sequence does not exceed 105 
Each element of each input sequence is non-negative integer not exceeding 1018. 
Each input sequence is a correct sequence of all K-sums with repetitions of some non-decreasing sequence of non-negative integers.

Sample Input

3
1 3
3
2 2
12 34 56
3 2
2 3 4 4 5 6
Sample Output

1
6 28
1 2 3
Explanation

Sample case #00: When N = 1 and K = 3 the only K-sum is S[1] = 3 * A[1]. Hence A[1] = S[1] / 3 = 3 / 3 = 1.

Sample case #01: Since 6 + 6 = 12, 6 + 28 = 34, 28 + 28 = 56, then Alice indeed could think of the sequence {6, 28}.

Sample case #02: It corresponds to the example in the problem statement.
Approach
Firstly, For a given N and K the number of terms in K-Sums sequence will be n+k-1 Choose k. 
Let these terms be M and represented by array Sums[] and original array be A[]
After sorting this Sums[] sequence we can say that A[0] = Sums[0]/K. And erase S[0] as it won't have information for any other terms in sequence A[].
Hence for any Sums[i] we note that after erasing all k-sums involving numbers a[0], a[1], ..., a[i-1] the minimal k-sum is a[i] + (k-1) * a[0], hence giving the next a[i] value.
We do the removing part using dynamic programming. Erasing all the terms in S[] that are made using previous K sum elements of A[] till A[i].
Also we don't need to erase k-sums that contain a[n-1] since we have already restored the whole array by then.
Problem Setter's code :
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

// returns n! / k! / (n-k)! = n * (n-1) * ... * (n-k+1) / 1 / 2 / ... / k
// = n / 1 * (n-1) / 2 * (n-2) / 3 * ... * (n-k+1) / k
int bin(int n, int k) {
    if(k > n - k) {
        k = n - k;
    }
    int p = 1;
    for (int i = 1; i <= k; ++i) {
        p *= n + 1 - i;
        p /= i;
    }
    return p;
}

int n, k;
LL a[100000];
multiset<LL> kSums;

// recursive routine that erase all sums having a[i] as the last element
// @j is the current a[j] we want to add to the sum
// @cnt is the count of numbers in the current sum
// @sum is the value of the sum
void rec(int i, int j, int cnt, LL sum) {
    if (cnt == k) {
        kSums.erase(kSums.find(sum));
    } else {
        rec(i, j, cnt + 1, sum + a[j]);
        if (j < i) {
            rec(i, j + 1, cnt, sum);
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    assert ( 1<=T<=100000);
    for (int t = 0; t < T; ++t) {
        // n and k defined globally
        scanf("%d%d", &n, &k);
        assert ( 1<=n<=100000);
        assert ( 1<=k<=100000);

        int m = bin(n + k - 1, k); // the total number of k-sums
        assert ( 1<=m<=100000);

        // input k-sums and insert them into multiset
        kSums.clear();
        for (int i = 0; i < m; ++i) {
            LL kSum;
            scanf("%lld", &kSum);
            assert ( 1<=kSum<=1000000000000000000L);
            kSums.insert(kSum);
        }

        // the minimal k-sum is alsways a[0] * k
        a[0] = *(kSums.begin()) / k;
        kSums.erase(kSums.begin());

        for (int i = 1; i < n; ++i) {

            // after erasing all k-sums involcing numbers a[0], a[1], ..., a[i-1]
            // the minimal k-sum is a[i] + (k-1) * a[0]
            a[i] = *(kSums.begin()) - (k - 1) * a[0];

            // we don't need to erase ksums that contain a[n-1]
            // since we have already restored the whole array
            // and this important in the case n=2 since k could be 99999 in this case
            // which could lead to stack overflow and TL
            if (i < n - 1) {
                rec(i, 0, 1, a[i]);
            }
        }

        for (int i = 0; i < n; ++i) {
            printf("%lld%c", a[i], i < n - 1 ? ' ' : '\n');
        }
    }
    return 0;
}
Problem Tester's code :
#include <cmath>
#include <set>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 100000

int n, k;
long long a[MAX];

multiset<long long> s;

void rec(int m, int idx, int at, long long sum) {
    if (at == k - 1) {
        s.erase(s.find(sum));
    }
    else {
        rec(m, idx, at + 1, sum + a[idx]);
        if (idx + 1 < m) {
            rec(m, idx + 1, at, sum);
        }
    }
}
int main() {
//    freopen("input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    while (T--) {
        s.clear();
        scanf("%d%d", &n, &k);
        char c;
        scanf("%c", &c);
        while (true) {
            long long temp;
            scanf("%lld%c", &temp, &c);
            s.insert(temp);
            if (c == '\n') break;
        }

        a[0] = *s.begin() / k;
        s.erase(s.begin());
        for (int i = 1; i < n; i++) {
            a[i] = ((*s.begin()) - a[0] * (k - 1));
            rec(i + 1, 0, 0, a[i]);
        }
        for (int i = 0; i < n - 1; i++) printf("%lld ", a[i]); printf("%lld\n", a[n - 1]);
    }
    return 0;
}
'''
def getPermutationUtil(N,nums,item,index,res):
    if len(item)==N:
        res.append(item)
        return
    if index>=len(nums):
        return
    getPermutationUtil(N, nums, item+[nums[index]], index+1,res)
    getPermutationUtil(N, nums, item, index+1, res)
    
def getPermutation(N,nums):
    res=[]
    used=[False] * len(nums)
    getPermutationUtil(N,nums,[],0,res)
    return res
def checkRes(res,nums):
    return True

def getOriginNums(N,K,nums):
    candidates=[]
    for num in nums:
        if num%K==0:
            candidates.append(num//K)
    candidates=sorted(candidates)
    print(candidates)
    if len(candidates)==N:
        return candidates
    res=[candidates[0],candidates[-1]]
    if N==2:
        return res
    candidates=candidates[1:-1]
    possibleReses=getPermutation(N-2, candidates)
    for possibleRes in possibleReses:
        res+=possibleRes
        if checkRes(res,nums):
            return res
            

# caseNum=int(input().strip())
# for caseindex in range(caseNum):
#     line1=input().strip().split(" ")
#     N,K=int(line1[0]),int(line1[1])
#     nums=[int(_) for _ in input().strip().split(" ")]
#     print(getOriginNums(N,K,nums))
N=3
K=2
nums=[2,3,4,4,5,6]
print(getPermutation(3, [1,2,4,5]))
print(getOriginNums(N, K, nums))