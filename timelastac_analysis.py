# -*- coding: utf-8 -*-
#统计一天中的144个时刻正在进行的活动

f=open("D:\\Data for bigdata\\hh115\\timelastac.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac_on_time.txt","w")
timeunit=600
output_time=0
last_day='2011-06-15'
current_ac=''
def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)+':'+str(s)
for line in f.readlines():
    aline=line.split()
    if(last_day!=aline[0]):
        while (output_time < 86400):
            fout.write(last_day + ' ' + secondstocolon(output_time) + ' ' + current_ac + '\n')
            output_time += timeunit
        output_time=0
        last_day=aline[0]
    while(output_time<int(aline[1])):
        fout.write(aline[0]+' '+secondstocolon(output_time)+' '+current_ac+'\n')
        output_time+=timeunit
    if(aline[3]=='end'):

        current_ac=''
    else:
        current_ac=aline[2]

f.close()
fout.close()
