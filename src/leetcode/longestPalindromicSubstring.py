'''
'''
from timeit import Timer
def longestPalindrome(s):
    
    if len(s)==0:
        return 0
    maxLen=1
    start=0
    for i in range(len(s)):
        if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
            start=i-maxLen-1
            maxLen+=2
            continue

        if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
            start=i-maxLen
            maxLen+=1
    return s[start:start+maxLen]
def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    """

    dp=[[False for col in range(len(s))] for row in range(len(s))]
    res=[0,0];
    for i in range(len(s)):
        dp[i][i]=True
        if i>1 and s[i]==s[i-1]:
            dp[i-1][i]=True
            res[0]=i-1
            res[1]=i
    for length in range(3,len(s)+1):
        for i in range(len(s)-length+1):
            j=i+length-1
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=True
                res[0]=i
                res[1]=j
    return s[res[0]:res[1]+1]

def longestPalindrome3( s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range (1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
s="lphbehiapswjudnbcossedgioawodnwdruaaxhbkwrxyzaxygmnjgwysafuqbmtzwdkihbwkrjefrsgjbrycembzzlwhxneiijgzidhngbmxwkhphoctpilgooitqbpjxhwrekiqupmlcvawaiposqttsdgzcsjqrmlgyvkkipfigttahljdhtksrozehkzgshekeaxezrswvtinyouomqybqsrtegwwqhqivgnyehpzrhgzckpnnpvajqevbzeksvbezoqygjtdouecnhpjibmsgmcqcgxwzlzztdneahixxhwwuehfsiqghgeunpxgvavqbqrelnvhnnyqnjqfysfltclzeoaletjfzskzvcdwhlbmwbdkxnyqappjzwlowslwcbbmcxoiqkjaqqwvkybimebapkorhfdzntodhpbhgmsspgkbetmgkqlolsltpulgsmyapgjeswazvhxedqsypejwuzlvegtusjcsoenrcmypexkjxyduohlvkhwbrtzjnarusbouwamazzejhnetfqbidalfomecehfmzqkhndpkxinzkpxvhwargbwvaeqbzdhxzmmeeozxxtzpylohvdwoqocvutcelgdsnmubyeeeufdaoznxpvdiwnkjliqtgcmvhilndcdelpnilszzerdcuokyhcxjuedjielvngarsgxkemvhlzuprywlypxeezaxoqfges"
print(s[::-1])
print(longestPalindrome(s))
print(longestPalindrome2(s))
print(longestPalindrome3(s))
# print(Timer('longestPalindrome2()','from __main__ import longestPalindrome2').timeit(1))print(Timer('longestPalindrome()','from __main__ import longestPalindrome').timeit(1))