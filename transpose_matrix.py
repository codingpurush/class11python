#normal
matrix=[[1,3,5],[2,5,9]]
for r in range(2):
  for c in range(3):
    print(matrix[r][c],end='  ')
  print()
  
#transpose
matrix=[[1,3,5],[2,5,9]]
for r in range(3):
  for c in range(2):
    print(matrix[c][r],end='  ')
  print()
