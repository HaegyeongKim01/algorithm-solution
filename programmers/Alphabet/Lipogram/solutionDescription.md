# :bulb: Lipogram - solution Desciprtion 
Pangram과 다르게 Lipogram은 모든 알파벳을 사용하지 않는 경우이다.    
다른 문제인 Pangram은 그저 pangram의 유무만 판단하는 문제였지만 Lopogram의 문제는 "YES"인 경우 사용하지 않은 알파벳도 출력해야한다.    

---
1. input받는다. `replace()`로 공백 제거 -> `lower()`로 모두 소문자로 변경 -> `list()`화     
2. `딕셔너리.values()`로 딕셔너리의 value들을 리스트로 가져오고 False인지 확인하여 Lipogram의 참/거짓 판단.     
3. Lipogram이 아닌 경우 그저 NO출력.     
4. Lipogram인 경우 `딕셔너리.items()`메소드를 사용하여 딕셔너리의 key와 value를 받아와서 value의 값의 False인 경우 key를 print한다. 

---
