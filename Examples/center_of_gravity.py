import numpy as np
import matplotlib.pyplot as plt
import math
from sympy import *

r=Symbol('r')
t=Symbol('t')
a=Symbol('a')

I1=integrate(cos(t)*r**2,(r,0,a*(1+cos(t))),(t,-pi,pi))
I2=integrate(r,(r,0,a*(1+cos(t))),(t,-pi,pi))
I=I1/I2
print(I)
I=I.subs(a,5)
plt.axes(projection='polar')
a=5

rad=np.arange(0,(2*np.pi),0.01)

# cardioid
for i in rad:
    r=a+(a*np.cos(i))
    plt.plot(i,r,'g.')

plt.polar(0,I,'r.')
plt.show()
