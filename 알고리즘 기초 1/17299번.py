# 오등큰수
import sys
input = sys.stdin.readline

count = [0] * 1000001
stack = []

n = int(input())
ngf = [-1] * n
num = list(map(int, input().split()))

# 숫자 등장 횟수 저장
for i in num:
    count[i] += 1


for i in range(n):
    # 스택이 존재하고, 현재 수열값의 등장횟수가 더 크면 
    while stack and count[num[stack[-1]]] < count[num[i]]:
        ngf[stack.pop()] = num[i]
    stack.append(i)

print(*ngf)
