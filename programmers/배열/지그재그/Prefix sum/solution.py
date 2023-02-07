import itertools 

n = int(input())

arr = list(map(int, input().split()))

acc_arr = itertools.accumulate(arr)

for a in acc_arr:
    print(a, end= " ")