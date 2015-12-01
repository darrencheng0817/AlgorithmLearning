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
@author: Darren
'''
