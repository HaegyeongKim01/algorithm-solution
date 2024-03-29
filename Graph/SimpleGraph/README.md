# **단순 그래프**

# **문제**

![https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/cbd970d6-2bde-484a-9508-6e87f49c8451/1.png](https://grepp-programmers.s3.ap-northeast-2.amazonaws.com/files/production/cbd970d6-2bde-484a-9508-6e87f49c8451/1.png)

*단순 그래프*(*Simple graph*)는 두 정점을 잇는 간선은 최대 한 개 존재하고, 자기 자신을 잇는 간선이 없는 그래프이다. 위 그래프는 정점 `2` 와 `3` 을 잇는 간선이 두 개 존재하는데다가 정점 `4` 와 `4` 를 잇는 간선도 존재하므로 *단순 그래프*(*Simple graph*)가 아니다.

그래프가 주어질 때, 이 그래프가 *단순 그래프*(*Simple graph*)인지 확인해보자.

### **힌트**

여러 코딩 테스트 문제에서 주어지는 그래프는 대부분 *단순 그래프*(*Simple graph*)이지만 그렇지 않을 수도 있기 때문에, 문제를 해결할 때 이를 적절히 고려해야 한다.

이 문제에서 주어진 그래프가 *단순 그래프*(*Simple graph*)인지 확인하기 위해서는 우선 *인접 행렬*(*Adjacency matrix*)이나 *인접 리스트*(*Adjacency list*)로 주어진 그래프를 저장해야 한다. 두 방법 모두 장단점이 존재하는 방법이기 때문에 문제의 조건에 따라 적절하게 선택해야 한다.

# **입력**

첫째 줄에 그래프의 정점의 개수와 간선의 개수 `N, M (1 ≤ N, M ≤ 50)` 이 주어진다. 그래프의 각 정점에는 `1` 부터 `N` 까지 번호가 매겨져 있다.

둘째 줄부터 `M` 개의 줄에 그래프의 간선이 주어진다. 간선은 두 정점 `U, V (1 ≤ U, V ≤ N)` 을 잇는다.

# **출력**

주어진 그래프가 *단순 그래프*(*Simple graph*)라면 `YES` 를 그렇지 않다면 `NO` 를 출력한다.

# **예제 입력 1**

```6 7
1 2
1 5
2 3
2 5
3 4
4 5
4 6 
``` 

# **예제 출력 1**

```
YES
```

# **예제 입력 2**

```6 6
1 5
2 3
2 5
3 2
3 6
5 6 
```

# **예제 출력 2**

```NO``` 

# **예제 입력 3**

```6 6
1 5
2 3
2 5
3 6
4 4
5 6
```  

# **예제 출력 3**

```NO```
