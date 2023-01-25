# New year money 
## 문제 접근 
`input`    
사람 수    
int_arr   
    
`output`   
int_arr 돌아가면서 자신 보다 작은 수 , 큰 수 출력   

      
원본 arr는 각 요소를 중심으로 smalll & big 판단하게 하기에 원본 arr를 for문을 도는데 사용하고, for문 밖에 sorted:정렬된 arr를 하나 만든다.       
이중 for문으로 원본 arr for문 안에 sorted된 sorted_arr와 조건 비교하여  big & small 판단 -> cnt++ (big||small)
