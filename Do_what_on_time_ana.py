# -*- coding: utf-8 -*-
#统计一天中的144个时刻正在进行的活动，最终统计
import matplotlib.pyplot as plt
f=open("D:\\Data for bigdata\\hh115\\ac_on_time.txt","r")
timeunit=600
draw_min_num=30
ac_list=['Sleep', 'Bed_Toilet_Transition', 'Toilet', 'Morning_Meds', 'Dress', 'Groom', 'Relax', 'Leave_Home', 'Enter_Home', 'Cook_Breakfast', 'Eat_Breakfast', 'Wash_Breakfast_Dishes', 'Watch_TV', 'Cook_Lunch', 'Eat_Lunch', 'Take_Medicine', 'Bathe', 'Evening_Meds', 'Personal_Hygiene', 'Read', 'Work', 'Entertain_Guests', 'Sleep_Out_Of_Bed', 'Eat', 'Cook', 'Cook_Dinner', 'Eat_Dinner', 'Wash_Dinner_Dishes', 'Exercise', 'Wash_Lunch_Dishes', 'Wash_Dishes', 'Make_Bed', 'Paramedics', 'Caregiver', 'g1.Housekeeping', 'r1.Enter_Home', 'r1.Work', 'r1.Relax', 'r1.Leave_Home', 'r1.Watch_TV', 'g1.Leave_Home', 'g1.Enter_Home', 'Groceries', 'Laundry', 'Piano', 'Housekeeping', 'Drug_Management', 'r1.Personal_Hygiene', 'r1.Dress', 'r1.Cook_Breakfast', 'r1.Eat_Breakfast', 'r1.Dishes', 'r1.Toilet', 'r1.Groom', 'Door_Ajar', 'Loose_Connection', 'g2.Enter_Home', 'g2.Leave_Home', 'System_Technicians', 'Started', 'g1.Maintenance', 'r1.Read', 'g1.Caregiver', 'g1.Movers', 'g1.Inspection']
def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)+':'+str(s)
def time2sec(time):
    timestr = time.split(':')
    return int(timestr[0])*3600+int(timestr[1])*60+int(timestr[2])
class timepoint:

    def __init__(self):
        self.time = 0
        self.ac_list = []
        self.ac_times_dic = {}

tp_dic={}
for i in range(86400/timeunit):
    tp=timepoint()
    tp.time=i*timeunit
    tp_dic[timeunit*i]=tp

for line in f.readlines():
    aline=line.split()
    if len(aline)==3:
        seconds=time2sec(aline[1])
        tp=tp_dic[seconds]
        if aline[2] not in tp.ac_list:
            tp.ac_list.append(aline[2])
            tp.ac_times_dic[aline[2]]=0
        else:
            tp.ac_times_dic[aline[2]] +=1

T_list=[]
ac_show_list=[]
for i in range(86400/timeunit):
    ACtimes=[]
    #print sorted(tp_dic[timeunit*i].ac_times_dic.items(),key=lambda item:item[1],reverse=1)
    for ac in ac_list:
        if tp_dic[timeunit*i].ac_times_dic.has_key(ac):
            ACtimes.append(tp_dic[timeunit*i].ac_times_dic[ac])
            if(tp_dic[timeunit*i].ac_times_dic[ac]>draw_min_num):
                if(ac not in ac_show_list):
                    ac_show_list.append(ac)
        else:
            ACtimes.append(0)
    T_list.append(ACtimes)

#ac_show_list=[]
for ac_show in ac_show_list:
    y=[]
    for line in T_list:
        y.append(line[ac_list.index(ac_show)])
    x=range(0,timeunit*len(T_list),timeunit)
    plt.plot(x,y,label=ac_list[ac_list.index(ac_show)])
plt.xlabel('time(seconds)')

plt.legend()
plt.show()

