r=int(input("rows: "))
c=int(input("columns: "))
matrix=[]
print("entre the values row wise: ")
for i in range(r):
  a=[]
  for j in range(c):
    a.append(int(input()))
  matrix.append(a)

print(matrix)
print()


for i in range(r):
  for j in range(c):
    print(matrix[i][j],end='  ')
  print()
