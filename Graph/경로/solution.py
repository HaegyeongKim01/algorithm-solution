n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

k = int(input())
path = list(map(int, input().split()))

for i in range(1, len(path)):
    if path[i] not in graph[path[i-1]]:
        print("NO")
        quit()

print("YES")
