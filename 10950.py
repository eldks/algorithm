num = int(input())
array = [0]*num
for i in range(num):
  a, b = input().split()
  a = int(a)
  b = int(b)
  array[i] = a+b

for j in range(num):
  print(array[j])