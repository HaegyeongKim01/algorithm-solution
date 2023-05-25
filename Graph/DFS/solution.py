def dfs(here):
    print(here, end=" ")
    visited[here] = True
    for v in sorted(graph[here]):
        if not visited[v]:
            visited[v] = True
            dfs(v)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

dfs(1)
