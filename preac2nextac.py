f=open("D:\\Data for bigdata\\hh115\\ac_day_seconds.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac2ac.txt","w")
def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)
day=''
last_ac=''
last_time=''
for line in f.readlines():
     aline=line.split()
     if(aline[1]!=day):
         fout.write(aline[1]+'*****************************************\n')
         day=aline[1]
     time=secondstocolon(int(aline[2]))
     fout.write(last_time+'->'+time+':'+last_ac+'->'+aline[0]+'\n')
     last_ac=aline[0]
     last_time=time

f.close()
fout.close()
