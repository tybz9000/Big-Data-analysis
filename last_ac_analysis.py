f=open("D:\\Data for bigdata\\hh115\\timelastac.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac_on_time2.txt","w")
def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)+':'+str(s)
ac_list=[]
timeunit=3600
output_time=0
last_day='2011-06-15'
current_ac=''
end=False
day=0
while(not end):
    line = f.readline()
    aline = line.split()
    if(aline[2]not in ac_list):
        ac_list.append(aline[2])
    if (aline[0] == '2012-04-19'):
        end = True
        break
    if (last_day != aline[0]):
        while (output_time <= 86400):
            if (current_ac != ''):
                fout.write(str(day)+' '+str(output_time/timeunit) + ' ' + str(ac_list.index(current_ac)) + '\n')
                #fout.write(str(output_time/timeunit) + ' ' + str(ac_list.index(current_ac)+1) + '\n')
            output_time += timeunit
        output_time = timeunit
        last_day = aline[0]
        day+=1
        if(day==83):
            print aline[0]
    while (output_time < int(aline[1])):
        if (current_ac != ''):
            fout.write(str(day)+' '+str(output_time/timeunit) + ' ' + str(ac_list.index(current_ac)) + '\n')
            #fout.write(str(output_time/timeunit) + ' ' + str(ac_list.index(current_ac)+1) + '\n')
        output_time += timeunit

    if aline[3] == 'begin':
        current_ac = aline[2]
    elif aline[3] == 'instant':
        #fout.write(last_day + ' ' + secondstocolon(output_time) + ' ' + aline[2] + '\n')
        current_ac = aline[2]

print ac_list
print len(ac_list)
f.close()
fout.close()