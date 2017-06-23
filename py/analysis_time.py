# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ac_day_seconds.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\action_analysis3.txt","w")
daydic={}
timedic={}
timesdic={}
permitdic={}
timetotaldic={}
ac_list=[]
day=''
for line in f.readlines():
     aline=line.split()
     if (day != aline[1]):
         for (k, v) in timetotaldic.items():
             if(timesdic[k]!=0):
                 timetotaldic[k] += timedic[k] / timesdic[k]

         for (k, v) in timedic.items():
             timedic[k]=0
         for (k, v) in permitdic.items():
             permitdic[k]=True
         for (k, v) in timesdic.items():
             timesdic[k]=0
         day=aline[1]

     if (aline[0] not in ac_list):
         ac_list.append(aline[0])
         timedic[aline[0]] = int(aline[2]) + int(aline[3]) / 2
         daydic[aline[0]] = 1
         permitdic[aline[0]]=False
         timesdic[aline[0]]=1
         timetotaldic[aline[0]]=0
     else:
         if(permitdic[aline[0]]==True):
             daydic[aline[0]]+=1
             permitdic[aline[0]]=False
         timedic[aline[0]]+=int(aline[2]) + int(aline[3]) / 2
         timesdic[aline[0]]+=1


for (k,v)in daydic.items():


    fout.write(k+":"+str(v)+'\n')
