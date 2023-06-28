from sympy import *
x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
a=2
b=3
c=4
w2=integrate(1,(z,0,c*(1-x/a-y/b)),(y,0,b*(1-x/a)),(x,0,a))
print(w2)