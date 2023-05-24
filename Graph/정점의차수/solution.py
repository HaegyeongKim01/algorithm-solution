#정점, 간선
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
res = 0 
for e in graph:
    res += len(e)

print(res)
