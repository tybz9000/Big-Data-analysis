# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ann.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac_day_seconds.txt","w")
time_dic_first={}
time_dic_last={}
ac_list=[]
last_ac=''
last_sc=0
last_day=''
def find_true_name(name):
    if '='in name:
        return name.split('=')[0]
    else:
        return name
def time2sec(time):
    timestr = time.split(':')
    return int(timestr[0])*3600+int(timestr[1])*60+int(timestr[2])

def truetime(time1,time2):
    if(time2>=time1):
        return time2-time1
    else:
        return time2-time1+3600*24

for line in f.readlines():
    aline=line.split()
    if(len(aline)==5):
        day=aline[0]
        time=aline[1].split('.')[0]
        realname=find_true_name(aline[4])
        seconds=time2sec(time)
        if (realname not in ac_list):
            ac_list.append(realname)
            time_dic_first[realname] = seconds
            time_dic_last[realname]=last_sc
        if (last_ac != realname and last_sc!=0):
            time_dic_first[realname]=seconds
            time_dic_last[last_ac]=last_sc
            if('.'not in last_ac):
                fout.write(last_ac+'     '+last_day+'     '+str(time_dic_first[last_ac])+'     '+str(truetime(time_dic_first[last_ac],time_dic_last[last_ac]))+'\n')
        last_ac=realname
        last_day=day
        last_sc=seconds

f.close()
fout.close()


