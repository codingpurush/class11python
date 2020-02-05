n = int(input())
a=-1
b=1
c=a+b
cnt=0
sum=0
for i in range(0,n):#(FIRST N TERMS)
#while(c<x):#(TERMS TILL N)
 print(c)
 cnt+=1
 sum+=c
 a=b
 b=c
 c=a+b
 
print("Number of terms printed : " )
print(cnt)
print("sum of the terms printed : ")
print(sum)
