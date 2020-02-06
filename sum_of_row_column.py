matrix=[[1,3,5],[2,5,9]]
for r in range(2):
  for c in range(3):
    print(matrix[r][c],end='  ')
  print()

print()
s=0
for r in range(2):
  for c in range(3):
   s+=matrix[r][c]
  print("sum of row ",r," is ",s)
  s=0
  print()

print()
s=0
for c in range(3):
  for r in range(2):
   s+=matrix[r][c]
  print("sum of column ",c," is ",s)
  s=0
  print()
