f=open("D:\\Data for bigdata\\hh115\\ac_on_time2.txt","r")
from PIL import Image
def setRBG(num):
    (a2,a3)=divmod(num,4)
    (a1,a2)=divmod(a2,4)
    return (a1*64,a2*64,a3*64)

x = 300
y = 150
n=43

c = Image.new("RGB", (x, y))
for line in f.readlines():
    aline=line.split()
    c.putpixel([int(aline[0]),int(aline[1])],setRBG(int(aline[2])))



c.show()
c.save('c.png')