# description 
a        =  Hpye  ,        Love  ,      Nxde      ,Antifragle ,  ShutDown       Love         
b        =  180,              178,      179,           ,185          ,176               

time_b = 1-180             181-358    359-537       538-722        723-898     899-1078                  
      =  180                358         537              722        898        1078     

if                           [i-1]+1 ~ [i]              

timeb = [0] #초기화                 
timeb식 = time_b[i-1] +b[i]                   
timeb == 노래 끝나는 시간을 저장해놓은 배열

## 구조 
main -> solution: calculate함수를 통해 timeb를 생성.        
if 물어보는 노래 길이 > 만들어진 timeb :  
 calculate 함수 호출로 timeb배열을 더 추가한다.     
만들어진 timeb에서 timeb의 조건으로 timeb에서 해당하는 *index* 를 찾고 찾은 *index*로 노래 제목을 a배열에서 찾아낸다. 

