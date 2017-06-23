# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ann.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ann_out.txt","w")
#活动对应的时间
Day=''
#重复检验时采用
Lastwork=''
#最后实际输出的活动
simplework=''
for line in f.readlines():
    aline=line.split()
    if(len(aline)==5):
        #时间标注
        if (Day != aline[0]):
            Day = aline[0]
            fout.write(Day + ':*******************************************\n')
        #获得实际活动内容
        if('='in aline[4]):
            simplework=aline[4].split('=')[0]
        else:
            simplework=aline[4]
        #活动去重且仅选择实验对象所进行的活动
        if(simplework!=Lastwork):
            Lastwork=simplework
            if('.'not in simplework):
                fout.write(simplework + '\n')

f.close()
fout.close()
