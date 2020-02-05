total=0
x=int(input())
for i in range(1,x+1):
  sum=0
  temp=i
  while i>0:
     r=i%10
     cube=r**3                   
     sum+=cube
     i=i//10
  if sum==temp:
     print(temp)
     total=total+temp
print("sum=", total)

      
