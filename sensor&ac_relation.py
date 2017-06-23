f=open("D:\\Data for bigdata\\hh115\\ac&sensor.txt","r")
fout=open("D:\\Data for bigdata\\hh115\\ac_sameas_ac.txt","w")
import numpy as np
class activity:
    def __init__(self):
        self.sensor_num=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
        self.one_sensor_num=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0]

def calEuclideanDistance(vec1,vec2):
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist
cur_ac=''
ac_list=[]
ac_dic={}
sensor_list=['M003', 'MA001', 'M005', 'MA008', 'MA012', 'MA002', 'M013', 'M010', 'D005', 'M007', 'M014', 'D002', 'M011', 'M015', 'M009', 'M006', 'M004', 'D003', 'D001', 'D004','system']
for line in f.readlines():
    if '***'in line:
        cur_ac=line.split()[0]
        if cur_ac not in ac_list:
            ac_list.append(cur_ac)
            ac_dic[cur_ac]=activity()
    else:
        sensor=line.split()[0]
        ac_dic[cur_ac].sensor_num[sensor_list.index(sensor)]+=1
for ac in ac_list:
    total=sum(ac_dic[ac].sensor_num)
    for i in range (len(ac_dic[ac].sensor_num)):
        ac_dic[ac].one_sensor_num[i]=round(float(ac_dic[ac].sensor_num[i])/total,3)

distance=[]
for ac in ac_list:
    dis=[]
    distance.append(dis)
    for ac2 in ac_list:
        v1=np.array(ac_dic[ac].one_sensor_num)
        v2=np.array(ac_dic[ac2].one_sensor_num)
        dist=calEuclideanDistance(v1,v2)
        dis.append(round(dist,3))

print len(ac_list)
print ac_list
for ac in ac_list:

    print ac+str(ac_list.index(ac))
    print ac_dic[ac].one_sensor_num
for line in distance:
    for adis in line:
        fout.write(str(adis)+' ')
    fout.write('\n')

f.close()
fout.close()