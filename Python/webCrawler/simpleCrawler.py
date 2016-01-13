'''
Created on 2016年1月12日

@author: Darren
'''

#encoding:UTF-8
import time
import urllib.request
import re 
from collections import deque
def crawlerData(url):
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
        print("not html")
        return
    
    # 避免程序异常中止, 用try..catch处理异常
    try:
        print("decoding")
        data = urlop.read().decode('utf-8')
    except:
        print("error decoding")
        return ""
    return data
def replace_html(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace('&#39;',' ')

    return s

def crawler(): 
    queue = deque()
    visited = set()
    
    url = "https://leetcode.com/problemset/algorithms/"
    cnt = 0
    visited |= {url}  # 标记为已访问
    
    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1

    data=crawlerData(url) 
 
    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href=\"/problems/(.+?)\"')
    for x in linkre.findall(data):
        if x not in visited:
            queue.append(x)
            print('加入队列 --->  ' + x)
    header="\'\'\'\nCreated on 1.12.2016\n\n@author: Darren\n\'\'\'"
    while queue:
        subUrl=queue.popleft()  # 队首元素出队
        url = "https://leetcode.com/problems/"+subUrl
        visited |= {url}  # 标记为已访问
        print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
        cnt += 1
        req = urllib.request.Request(url, headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        data=crawlerData(req) 
        startIndex=data.find('\"description\" content=\"')
        if startIndex>0:
            index=startIndex+1
            while True:
                if index>len(data):
                    break
                if data[index]=="/" and data[index+1]==">":
                    break
                index+=1
            result=data[startIndex+len('\"description\" content=\"'):index]
            result=replace_html(result)
            fileName=subUrl.replace('-',' ').title().replace(' ','').replace('/','')
            file_object = open(fileName+".py", 'w')
            try:
                file_object.write(header+"\'\'\'\n"+result+"\n\'\'\'\n")
            except:
                print("error in " +fileName)
            finally:
                file_object.close()
        time.sleep(10)
crawler()
