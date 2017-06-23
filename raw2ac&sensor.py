# -*- coding: utf-8 -*-
f=open("D:\\Data for bigdata\\hh115\\ann.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac&sensor.txt","w")
output_permit=False
for line in f.readlines():
    aline=line.split()
    if(len(aline)==5 and '.'not in aline[4]):
        if('begin'in aline[4]):
            fout.write(aline[4].split('=')[0] + ' ******************************************\n')
            output_permit=True
        elif('end'in aline[4]):
            output_permit=False
        else:
            if(('ON'in aline[3] and 'M'in aline[2])  or ('OPEN' in aline[3] and 'D' in aline[2]) or 'system'in aline[2]):
                fout.write(aline[4] + ' ******************************************\n')
                fout.write(aline[2] + '\n')
        #时间标注
    elif(len(aline)==4):
        if(output_permit):
            if (('ON'in aline[3] and 'M'in aline[2]) or ('OPEN' in aline[3] and 'D' in aline[2])):
                fout.write(aline[2] + '\n')
f.close()
fout.close()
