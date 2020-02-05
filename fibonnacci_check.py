x = int(input())
a=-1
b=1
c=a+b             #check fibonacci
while(c<x):
 a=b
 b=c
 c=a+b
if (c==x):
  print("Y")
else:
  print("N")
