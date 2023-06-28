from sympy import *
x,y,z=symbols('x y z')
i=integrate(exp(x+y+z),(z,0,(x+log(y))),(y,0,x),(x,0,log(2)))
print("%.4f" %float(i))