# -*- coding: utf-8 -*-
#统计一天中的144个时间进行了的活动
ac_list=['Sleep', 'Bed_Toilet_Transition', 'Toilet', 'Morning_Meds', 'Dress', 'Groom', 'Relax', 'Leave_Home', 'Enter_Home', 'Cook_Breakfast', 'Eat_Breakfast', 'Wash_Breakfast_Dishes', 'Watch_TV', 'Cook_Lunch', 'Eat_Lunch', 'Take_Medicine', 'Bathe', 'Evening_Meds', 'Personal_Hygiene', 'Read', 'Work', 'Entertain_Guests', 'Sleep_Out_Of_Bed', 'Eat', 'Cook', 'Cook_Dinner', 'Eat_Dinner', 'Wash_Dinner_Dishes', 'Exercise', 'Wash_Lunch_Dishes', 'Wash_Dishes', 'Make_Bed', 'Paramedics', 'Caregiver', 'g1.Housekeeping', 'r1.Enter_Home', 'r1.Work', 'r1.Relax', 'r1.Leave_Home', 'r1.Watch_TV', 'g1.Leave_Home', 'g1.Enter_Home', 'Groceries', 'Laundry', 'Piano', 'Housekeeping', 'Drug_Management', 'r1.Personal_Hygiene', 'r1.Dress', 'r1.Cook_Breakfast', 'r1.Eat_Breakfast', 'r1.Dishes', 'r1.Toilet', 'r1.Groom', 'Door_Ajar', 'Loose_Connection', 'g2.Enter_Home', 'g2.Leave_Home', 'System_Technicians', 'Started', 'g1.Maintenance', 'r1.Read', 'g1.Caregiver', 'g1.Movers', 'g1.Inspection']

f=open("D:\\Data for bigdata\\hh115\\timelastac.txt","r")
timeunit=600
output_time=timeunit
last_day='2011-06-15'
current_ac=''
end=False
def secondstocolon(seconds):
    (m,s)=divmod(seconds,60)
    (h,m)=divmod(m,60)
    return str(h)+':'+str(m)+':'+str(s)

class timepoint:
    def __init__(self):
        self.ac_times_dic = {}
tp_dic={}
for i in range(86400/timeunit):
    tp=timepoint()
    tp_dic[timeunit*(i+1)]=tp

while(not end):
    line=f.readline()
    aline=line.split()
    if(aline[0]=='2012-04-29'):
        end=True
        break
    if(last_day!=aline[0]):
        output_time=timeunit
        last_day=aline[0]
    while(output_time<int(aline[1])):
        if(current_ac!=''):
            if(not tp_dic[output_time].ac_times_dic.has_key(current_ac)):
                tp_dic[output_time].ac_times_dic[current_ac]=1
            else:
                tp_dic[output_time].ac_times_dic[current_ac]+=1
        output_time+=timeunit

    if aline[3]=='begin':
        current_ac=aline[2]

    elif aline[3]=='end':
        current_ac=''
        if (not tp_dic[output_time].ac_times_dic.has_key(aline[2])):
            tp_dic[output_time].ac_times_dic[aline[2]] = 1
        else:
            tp_dic[output_time].ac_times_dic[aline[2]] += 1
    elif aline[3]=='instant':
        if (not tp_dic[output_time].ac_times_dic.has_key(aline[2])):
            tp_dic[output_time].ac_times_dic[aline[2]] = 1
        else:
            tp_dic[output_time].ac_times_dic[aline[2]] += 1
        current_ac=''

T_list=[]
for i in range(86400/timeunit):
    ACtimes=[]
    print sorted(tp_dic[timeunit*(i+1)].ac_times_dic.items(),key=lambda item:item[1],reverse=1)


f.close()

