s=0
a=input()
for i in a:
  i=int(i)
  f=1
  for j in range(1,i+1):
    f=f*j
  s+=f
print(s==int(a))
