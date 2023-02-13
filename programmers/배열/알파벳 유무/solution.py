def solution():
   s, e = map(int, input().split(' '))
   s = s-1
   print(arr[s:e].count('e'))

n, m = map(int, input().split())
arr = list(input())
for _ in range(m):
    solution()