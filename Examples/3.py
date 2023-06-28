from sympy import *
x=Symbol('x')
y=Symbol('y')
z=Symbol('z')
w3=integrate(x**2+y**2,y,x)
print(w3)
w4=integrate(x**2+y**2,x,y)
print(w4)