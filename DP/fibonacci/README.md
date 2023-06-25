# 피보나치 수열

# **문제**

피보나치 수열은 `F[i] = F[i - 1] + F[i - 2]` 로 정의되는 수열이다. 첫 두 항은 조금씩 다르게 정의할 수도 있다. 다음과 같은 알고리즘으로 피보나치 수열을 구할 수도 있다.

`A = 1` , `B = 2` 로 초기화 한다. `A + B` 를 계산한 결과를 `A` 와 `B` 중에 작은 곳에 덮어쓴다.

위 알고리즘을 `N` 번 반복했을 때, 과정을 모두 구해보자.

# **입력**

첫째 줄에 정수 `N (1 ≤ N ≤ 20)` 이 주어진다.

# **출력**

초기 과정부터 시작해서 위 알고리즘을 `N` 번 적용하는 과정을 모두 출력한다.

# **예제 입력 1**

```5```

# **예제 출력 1**

```
1 2  
3 2  
3 5  
8 5  
8 13 
21 13
```