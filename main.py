import requests
import time
import os
from pyquery import PyQuery as pq
tl = []
cs = int(input('请输入次数：'))
jg = float(input('请输入间隔：'))

for i in range(0,cs):
    time.sleep(jg)
    r = requests.get('https://www.mcmod.cn/v1/')
    text = pq(str(r.text)).text()
    if (tl.append(text)) in (tl):
        continue
    print(f'{i+1}.{text} {i+1}/{cs}')
    f = open('奇奇怪怪.txt','a',encoding='utf-8')
    f.write(''+text + '\n')
    f.close()

def remove_duplicates():
    f_read=open(r'./奇奇怪怪.txt','r',encoding='utf-8') 
    f_write=open(f'./OUT-{cs}.txt','w',encoding='utf-8') 
    data=set()
    for a in [a.strip('\n') for a in list(f_read)]:
        if a not in data:
            f_write.write(a+'\n')
            data.add(a)
    f_read.close()
    f_write.close()

remove_duplicates()
print('OK!')
os.system('pause')
