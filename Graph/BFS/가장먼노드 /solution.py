from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for i in range(n+1)]
    visited = [-1] * (n+1)
    
    #인접리스트로 그래프 구성 
    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
    
    queue = deque([1])
    visited[1] = 0
    
    #BFS 수행 
    while queue:
        v = queue.popleft()
        
        for i in adj[v]:
            if visited[i] == -1:  #방문하지 않은 노드 
                queue.append(i)
                visited[i] = visited[v] +1
    #멀리 떨어진 노드 find
    for distance in visited:
        if distance == max(visited):
            answer += 1
            
    return answer
                
