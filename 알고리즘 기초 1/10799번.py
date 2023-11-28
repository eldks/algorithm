stack = []
result = 0
exp = input()

for i in range(len(exp)):
    if exp[i] == '(':
        stack.append('(')
    else:
        # () -> 레이저
        if exp[i-1] == '(':
            stack.pop()
            result += len(stack)
        
        # )) -> 막대 끝부분
        else:
            # 막대 하나는 더 이상 자를 수 없으므로 pop 해줘야 함 
            stack.pop()
            result += 1

print(result)

