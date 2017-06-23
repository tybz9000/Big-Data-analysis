# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ann.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\timelastac.txt","w")

def time2sec(time):
    timestr = time.split(':')
    return int(timestr[0])*3600+int(timestr[1])*60+int(timestr[2])

def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)+':'+str(s)

for line in f.readlines():
    aline=line.split()
    if len(aline)==5:
        if('.'in aline[4]):
            continue
        time = aline[1].split('.')[0]
        seconds = time2sec(time)
        if '=' in aline[4]:

            ac=aline[4].split('=')[0]
            if('begin'in aline[4]):
                be='begin'
            else:
                be='end'
            fout.write(aline[0]+' '+str(seconds)+' '+ac+' '+be+'\n')
        #时间分析时启用
        else:
            fout.write(aline[0]+' '+str(seconds)+' '+aline[4]+' '+'instant'+'\n')

f.close()
fout.close()
