# Snow solutionDescription 
`arr`
00 01 02
10 11 12   
20 21 22   

(r1, c1), (r2, c2)    

input n을 받으면 n*n의 배열을 *로 초기화!     
행, 열 입력 받음 => 사람좌표 기준 y, x     
<img src="https://user-images.githubusercontent.com/110768149/215086415-50acddde-01d0-4be3-b392-411398f0bb0d.png">

### 좌표의 여러 case가 존재 
<img src="https://user-images.githubusercontent.com/110768149/215086297-8c0392fd-06d5-4f54-828d-f15604166e6e.png">

//제설 수행시 좌표의 case에 따라 for문의 시작 위치 등이 달라질 수 있으나     
r1, r2 || c1, c2 값을 change함으로 대체    
//제설 수행
```
for y in range(r1, len(r2)+1):    
    for x in range(c1, len(c2)+1):    
        arrr[y][x] = "."   
```
