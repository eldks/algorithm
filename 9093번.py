import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
  text = input().rstrip()
  word = list(text.split())
  reverse = []

  for j in word:
    reverse.append(j[::-1])

  result = " ".join(reverse)
  print(result)
