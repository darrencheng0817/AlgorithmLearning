'''
Created on 2016年2月3日
给个图，每个节点有value，还有是否是surface （boolean值）。找到一个起点和终点都在surface的path，使得path上的所有节点和最大。
@author: Darren
'''
def add_end(L=None):
    print(L)
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())