def solution(x, y):
    global cnt
    if (y+1) < m and arr[x][y+1] ==1:
        cnt += 1
        solution(x, y+1)
    elif (x+1) < n and arr[x+1][y] == 1:
        solution(x+1, y)
        cnt += 1

n, m = map(int, input().split(' '))
arr = []
cnt = 0
for i in range(n):
    arr.append(list(map(int, input())))

solution(0, 0)
print(cnt+1)
