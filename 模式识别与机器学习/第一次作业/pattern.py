import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math
c11 = np.mat([0,0]).T
c12 = np.mat([2,0]).T
c13 = np.mat([2,2]).T
c14 = np.mat([0,2]).T
w1 = [c11,c12,c13,c14]
c21 = np.mat([4,4]).T
c22 = np.mat([6,4]).T
c23 = np.mat([6,6]).T
c24 = np.mat([4,6]).T
w2 = [c21,c22,c23,c24]
m1=(c11+c12+c13+c14)/4
m2=(c21+c22+c23+c24)/4
m= [m1,m2]
for i in [1,2]:
    if i==1:
        temp=np.zeros((2,2))            
        for j in range(0,4):
             temp=+temp+(w1[j]-m1)*(w1[j]-m1).T
        c1=temp/4
    if i==2:
        temp=np.zeros((2,2))            
        for j in range(0,4):
             temp=+temp+(w2[j]-m2)*(w2[j]-m2).T
        c2=temp/4
c=c1    
b=m1.T*c*m1+m2.T*c*m2
b/=2
a=(m1-m2).T*c
#表达式为 4x1+4x2=26    x1=(-4x2+26)/4
plt.figure(1)
x=[]
y=[]
a=np.linspace(0,10,100)
for i in a:
    x.append(i)
    y.append((-4*i+26)/4)
plt.plot(x,y)
plt.show()
