import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  test = input()
  stack = []
  status = True
  
  for i in test:
    if i == "(":
      stack.append(i)
      
    elif i == ")":
      if len(stack) == 0:
        print("NO")
        status = False
        break
        
      else:
        stack.pop()

  if status == True:
    if len(stack) == 0:
      print("YES")
      
    else:
      print("NO")
        
