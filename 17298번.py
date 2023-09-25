import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and nums[i]>nums[stack[-1]]:

        result[stack[-1]]=nums[i] 

        stack.pop() 

    stack.append(i)
print(*result)
## 파이썬에서 *는 unpacking 역할
## result 안의 데이터를 풀어 각각으로
