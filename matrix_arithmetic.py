matrix1=[[1,3,5],[2,5,9]]
for r in range(2):
  for c in range(3):
    print(matrix1[r][c],end='  ')
  print()

print()

matrix2=[[1,1,1],[1,1,1]]
for r in range(2):
  for c in range(3):
    print(matrix2[r][c],end='  ')
  print()

for r in range(2):
  for c in range(3):
    matrix1[r][c]=matrix1[r][c]+matrix2[r][c]  #change=,-,*,/ here

print()
print("sum is : ")

print()
for r in range(2):
  for c in range(3):
    print(matrix1[r][c],end='  ')
  print()
