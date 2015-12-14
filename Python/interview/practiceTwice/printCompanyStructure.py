'''
Created on 2015年12月1日
Employee,Manager,ItemsSold
Alice,,5
Bob,Alice,3
Carol,Bob,2
Richard,Carol,5
Kim,Richard,5
Tom,Carol,5
David,Bob,3
Eve,Alice,2
Ferris,Eve,1
就是员工跟他的manager还有销售的item，之后输出下面的结构，数字表示该员工跟他下属的sold item总额
Alice 31
|-Bob 23
| |-Carol 17
| | |-Richard 10
| | | \_Kim 5
| | \_Tom 5
| \_David 3
\_Eve 3
  \_Ferris 1
解法：这题略坑，算法就是先建图然后跑dfs，主要是output很恶心，output也是用dfs做的
如果当前节点是父节点的最后一个child，必须变成\_。
其实这个并不是很难，楼主当时脑残了，只需要把父节点的prefix和当前节点是否是最后节点一起传下去就好了。
test case
10
Alice,,5
Carol,Bob,2
Bob,Alice,3
Richard,Carol,5
Kim,Richard,5
Darren,Alice,2
Tom,Carol,5
David,Bob,3
Eve,Alice,2
Ferris,Eve,1

@author: Darren
'''

    