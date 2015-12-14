'''
Created on 2015年12月1日
n叉树判断是否有回路，dfs, 但是不希望一直维护一个祖先节点的哈希表，所以可以设计一个类，里面存一个布尔型的变量，访问过的设为true，回溯之后设为false
same as https://leetcode.com/problems/course-schedule/
https://leetcode.com/problems/course-schedule-ii/
@author: Darren
'''
