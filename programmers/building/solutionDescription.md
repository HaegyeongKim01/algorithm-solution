# 빌딩
`input`   
: n   
: arr   

`output`      
: 왼쪽에 보는 cnt, 오른쪽에서 보는 cnt    

left_cnt = count_building()   
right_cnt = count_building()   

def:  for문 돌리는 매개변수로 왼->오 , 오->왼   
cnt = 0   
if 오른쪽:   
    reversed(arr)   
for a in arr:   
    if maxlayer < a:   
        cnt += 1   
return cnt    
