#@title 音频下载
%cd /content/

import requests,re,json
!rm -rf /content/audio/*

#

def download(downType,url):
    !mkdir -p /content/audio
    if downType==0:
        v=open(f'./audio/jh.mp3','wb')
        b=requests.get(url).content
        v.write(b)
        v.close()
    elif downType==1:
        a=0
        d=requests.get(url).text
        rex='(https://static.wikia.nocookie.ne.*?)"'
        d=set(re.findall(rex,d))
        for i in d:
            print(a)
            a+=1
            v=open(f'./audio/{a}.ogg','wb')
            b=requests.get(i).content
            v.write(b)
            v.close()
    return 



#
def nameAndTrain(name):
    with open('name.txt','w',encoding='utf8') as f:
        f.write(name)
    !python cmdui.py
    return
#

f=open('/content/drive/MyDrive/tasklist.json','r',encoding='utf8')
d=json.load(f)
f.close()
for i in d:
    name=i[0]
    downType=i[1]
    url=i[2]
    !rm -rf /content/audio/*
    download(downType,url)
    nameAndTrain(name)
    print(f'已完成训练：{str(i)}')
    !rm -rf /content/GPT-SoVITS/output/*


