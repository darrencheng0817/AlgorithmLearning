'''
Created on 2015年12月1日

@author: Darren
'''
'''
Java Code
import java.util.BitSet;

publicclass BloomFilter 
{
/* BitSet初始分配2^24个bit */ 
privatestaticfinalint DEFAULT_SIZE =1<<25; 
/* 不同哈希函数的种子，一般应取质数 */
privatestaticfinalint[] seeds =newint[] { 5, 7, 11, 13, 31, 37, 61 };
private BitSet bits =new BitSet(DEFAULT_SIZE);
/* 哈希函数对象 */ 
private SimpleHash[] func =new SimpleHash[seeds.length];

public BloomFilter() 
{
for (int i =0; i < seeds.length; i++)
{
func[i] =new SimpleHash(DEFAULT_SIZE, seeds[i]);
}
}

// 将字符串标记到bits中
publicvoid add(String value) 
{
for (SimpleHash f : func) 
{
bits.set(f.hash(value), true);
}
}

//判断字符串是否已经被bits标记
publicboolean contains(String value) 
{
if (value ==null) 
{
returnfalse;
}
boolean ret =true;
for (SimpleHash f : func) 
{
ret = ret && bits.get(f.hash(value));
}
return ret;
}

/* 哈希函数类 */
publicstaticclass SimpleHash 
{
privateint cap;
privateint seed;

public SimpleHash(int cap, int seed) 
{
this.cap = cap;
this.seed = seed;
}

//hash函数，采用简单的加权和hash
publicint hash(String value) 
{
int result =0;
int len = value.length();
for (int i =0; i < len; i++) 
{
result = seed * result + value.charAt(i);
}
return (cap -1) & result;
}
}
}
'''
# _*_coding:utf_8_

class SimpleHash():  
    
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
    
    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return (self.cap - 1) & ret    

class BloomFilter():
    
    def __init__(self, BIT_SIZE=1 << 25):
        self.BIT_SIZE = BIT_SIZE
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.bitset = [False] * (self.BIT_SIZE)
        self.hashFunc = []
        
        for i in range(len(self.seeds)):
            self.hashFunc.append(SimpleHash(self.BIT_SIZE, self.seeds[i]))
        
    def insert(self, value):
        for f in self.hashFunc:
            loc = f.hash(value)
            self.bitset[loc] = True
            
    def isContaions(self, value):
        if value == None:
            return False
        ret = True
        for f in self.hashFunc:
            loc = f.hash(value)
            ret = ret & self.bitset[loc]
        return ret

def main():
    bloomfilter = BloomFilter()
    while True:
        # url = raw_input()
        url = input("Enter urls:")
        if url == 'exit':  # if url is equal exit break
            break
        if bloomfilter.isContaions(url) == False:
            bloomfilter.insert(url)
        else:
            print('url :%s has exist' % url) 
            
main()
