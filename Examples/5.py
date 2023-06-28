from sympy import *
r=Symbol('r')
t=Symbol('t')
a=Symbol('a')
w3=2*integrate(r,(r,0,a*(1+cos(t))),(t,0,pi))
print(w3)