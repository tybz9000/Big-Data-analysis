# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ann_out.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\1d_analysis_ac.txt","w")
ac_list=[]
ac_dic={}
day_count=0
for line in f.readlines():
    if '***' in line:
        day_count+=1
    if '***' not in line:
        if(line not in ac_list):
            ac_list.append(line)
            ac_dic[line]=1
        else:
            ac_dic[line]+=1



fout.write('天数:'+str(day_count)+'\n')
fout.write('活动种类:'+str(len(ac_list))+'\n')
for (k,v)in ac_dic.items():
    fout.write(k+str(v)+'\n')
print ac_dic
