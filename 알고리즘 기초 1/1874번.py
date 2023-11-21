count = 1
stack = []
result = []
temp = True

n = int(input())
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")

    else:
        temp = False

if temp == True:
    for i in result:
        # print(result[i])
        print(i)

else:
    print("NO") 