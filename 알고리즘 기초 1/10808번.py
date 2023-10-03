import sys
input = sys.stdin.readline

word = input().rstrip()
stack = [0]*26

for i in word:
  stack[ord(i) - 97] += 1

for i in stack:
  print(i, end=' ')
