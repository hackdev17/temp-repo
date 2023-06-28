from sympy import *
x,y=symbols('x y')
i=integrate((x+y),(y,0,x),(x,0,1))
print(float(i))