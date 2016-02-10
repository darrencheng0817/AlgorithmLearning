'''
Created on 2016年2月9日

@author: Darren
'''
'''
Name That Number
Among the large Wisconsin cattle ranchers, it is customary to brand cows with serial numbers to please the Accounting Department. The cow hands don't appreciate the advantage of this filing system, though, and wish to call the members of their herd by a pleasing name rather than saying, "C'mon, #4734, get along."

Help the poor cowhands out by writing a program that will translate the brand serial number of a cow into possible names uniquely associated with that serial number. Since the cow hands all have cellular saddle phones these days, use the standard Touch-Tone(R) telephone keypad mapping to get from numbers to letters (except for "Q" and "Z"):

          2: A,B,C     5: J,K,L    8: T,U,V
          3: D,E,F     6: M,N,O    9: W,X,Y
          4: G,H,I     7: P,R,S
Acceptable names for cattle are provided to you in a file named "dict.txt", which contains a list of fewer than 5,000 acceptable cattle names (all letters capitalized). Take a cow's brand number and report which of all the possible words to which that number maps are in the given dictionary which is supplied as dict.txt in the grading environment (and is sorted into ascending order).

For instance, the brand number 4734 produces all the following names:

GPDG GPDH GPDI GPEG GPEH GPEI GPFG GPFH GPFI GRDG GRDH GRDI
GREG GREH GREI GRFG GRFH GRFI GSDG GSDH GSDI GSEG GSEH GSEI
GSFG GSFH GSFI HPDG HPDH HPDI HPEG HPEH HPEI HPFG HPFH HPFI
HRDG HRDH HRDI HREG HREH HREI HRFG HRFH HRFI HSDG HSDH HSDI
HSEG HSEH HSEI HSFG HSFH HSFI IPDG IPDH IPDI IPEG IPEH IPEI
IPFG IPFH IPFI IRDG IRDH IRDI IREG IREH IREI IRFG IRFH IRFI
ISDG ISDH ISDI ISEG ISEH ISEI ISFG ISFH ISFI
As it happens, the only one of these 81 names that is in the list of valid names is "GREG".

Write a program that is given the brand number of a cow and prints all the valid names that can be generated from that brand number or ``NONE'' if there are no valid names. Serial numbers can be as many as a dozen digits long.

PROGRAM NAME: namenum

INPUT FORMAT

A single line with a number from 1 through 12 digits in length.
SAMPLE INPUT (file namenum.in)

4734
OUTPUT FORMAT

A list of valid names that can be generated from the input, one per line, in ascending alphabetical order.
SAMPLE OUTPUT (file namenum.out)

GREG
'''

def load_dict(file_name):
    file = open(file_name,"r",newline="\n")
    names=list(file.readlines())
    for index,name in enumerate(names):
        names[index] = name[:-2]
    d=set(names)
    return d

def namenum(nums):
    d=load_dict("namenumdict.txt")
    m={"2":"ABC","3":"DEF","4":"GHI","5":"JKL","6":"MNO","7":"PRS","8":"TUV","9":"WXY"}
    candidates=[""]
    for num in nums:
        temp=[]
        for candidate in candidates:
            for char in m[num]:
                temp.append(candidate+char)
        candidates=temp
    res=[]
    for candidate in candidates:
        if candidate in d:
            res.append(candidate)
    if not res:
        res.append("NONE")
    print(res)
    
namenum("426")