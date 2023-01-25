n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)
for a in arr:
    small_cnt, big_cnt = 0, 0
    
    for i in range(len(sorted_arr)):
        if sorted_arr[i] < a :
            small_cnt += 1
            
        elif sorted_arr[i] > a:
            big_cnt += 1
    print(small_cnt, big_cnt )