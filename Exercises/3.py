from sympy import *
x,y=symbols('x y')
i=integrate(1,(x,0,sqrt(16-y**2)),(y,0,4))
print(i)