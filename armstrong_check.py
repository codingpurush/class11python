sum=0
n=int(input())
a=len(str(n))
temp=n
while (temp>0):
 r=temp%10
 sum+=(r**a)
 temp=temp//10
print(sum==n)
