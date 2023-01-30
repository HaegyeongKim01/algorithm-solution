# :bulb: pangram 
## SolutionDescription
**pangram: 모든 알파벳이 존재**

from string import ascii_lowercase
`ascii_lowercase` 라이브러리 사용!    
import 한 후 바로 ascii_lowercase를 필드처럼 사용하면 된다.   
입력을 받을 때 여러 단어가 뭉쳐서 하나의 문자열로 입력 받기에 아래와 같은 순서로 코드를 수행하도록 한다.    
<br>   
**알파벳 유무 적용**    
```
1. input()
2. 공백제거  -> replace() 사용       
3. 소문자로 모두 change -> lower() 사용   
4. list화 -> list() 사용  
=> s = list(input().replace(' ', '').lower())
```

    
**pangram판단**    
만들어 놓은 딕셔너리(:alphabet)에 False가 존재한다면 pangram 아니다.       
✅<span style ="> 딕셔너리의 values()메소드 사용하면 리스트 반환! </span>  
```
if False in s.values():
  print("NO")
else:
  print("YES")
```
