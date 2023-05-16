n, m = map(int, input().split())
#0은 비워 두기 
arr = [[0 for i in range(n+1)] for i in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u][v] += 1
    arr[v][u] += 1

for row in arr:
    if max(row) > 1:
        print("NO")
        quit()

print("YES")
