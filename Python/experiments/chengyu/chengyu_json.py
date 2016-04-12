'''
Created on 2016年4月10日

@author: Darren
'''
class ChengYu(object):
    def __init__(self,chengyu, pinyin, jieshi, chuchu, lizi, spinyin):
        self.chengyu=chengyu
        self.pinyin=pinyin
        self.jieshi=jieshi
        self.chuchu=chuchu
        self.lizi=lizi
        self.spinyin=spinyin
        
import json
data={}
f=open('chengyu_data.txt','r',encoding='utf-8')
all_data=f.readlines()
for line in all_data:
    line=line.strip().split("',")
    if len(line)!=6:
        continue
    chengyu={'chengyu':line[0].split("'")[1],
             'pinyin':line[1].split("'")[1].split(),
             'jieshi':line[2].split("'")[1],
             'chuchu':line[3].split("'")[1],
             'lizi':line[4].split("'")[1],
             'spinyin':line[5].split("'")[1]
             }
    data[line[0].split("'")[1]]=chengyu
f.close()
f=open('chengyu_data.json','w',encoding='utf-8')
f.write(json.dumps(data,ensure_ascii=False,indent=4))
f.close()
chengyu_start={}
for key,value in data.items():
    if key[0] not in chengyu_start:
        chengyu_start[key[0]]=[]
    chengyu_start[key[0]].append(key)
for key,value in chengyu_start.items():
    chengyu_start[key]=sorted(chengyu_start[key], key=lambda x:len(chengyu_start[x[-1]]) if x[-1] in chengyu_start else 0)
f=open('chengyu_start.json','w',encoding='utf-8')
f.write(json.dumps(chengyu_start,ensure_ascii=False,indent=4))
f.close()
chengyu_start_pinyin={}
for key,value in data.items():
    if value['pinyin'][0] not in chengyu_start_pinyin:
        chengyu_start_pinyin[value['pinyin'][0]]=[]
    chengyu_start_pinyin[value['pinyin'][0]].append(key)
for key,value in chengyu_start_pinyin.items():
    chengyu_start_pinyin[key]=sorted(chengyu_start_pinyin[key], key=lambda x:len(chengyu_start[x[-1]]) if x[-1] in chengyu_start else 0)
f=open('chengyu_start_pinyin.json','w',encoding='utf-8')
f.write(json.dumps(chengyu_start_pinyin,ensure_ascii=False,indent=4))
f.close()