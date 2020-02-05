#PRINT Nth FIBONACCI NUMBER
x=int(input())
a=-1
b=1
c=a+b
for i in range(2,x+1):
 #print(c)
 a=b
 b=c
 c=a+b
if(i==x):
 print(c)
