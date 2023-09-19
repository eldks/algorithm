n, m = map(int, input().split())
a, b = [], []

for item in range(n):
  item = list(map(int, input().split()))
  a.append(item)

for item in range(n):
  item = list(map(int, input().split()))
  b.append(item)

for i in range(n):
  for j in range(m):
    print(a[i][j] + b[i][j], end=' ')

