stack = list()

cmd = list(input())

for elem in cmd:
    if elem == ')' and stack and stack[-1] =='(':
        stack.pop()
    else:
        stack.append(elem)

if stack:
    print("NO")
else:
    print("YES")
