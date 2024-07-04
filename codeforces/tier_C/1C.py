
from math import *
#Points:->
p =[list(map(float,input().split())) for i in range(3)]
#Sides:->
a,b,c=[hypot(x1-x2,y1-y2) for (x1,y1),(x2,y2) in [(p[0],p[1]),(p[0],p[2]),(p[1],p[2])]]
#Angles:->
A,B,C=[acos((y*y+z*z-x*x)/2/z/y) for x,y,z in [(a,b,c),(b,c,a),(c,a,b)]]
#Radius:->
R=a/2/sin(A)
#get_n ABC
def g(x,y):
    return x if y<1e-3 else g(y,fmod(x,y))
#n
u=2*g(A,g(B,C))
print(round(R * R * pi / u * sin(u),7)) 