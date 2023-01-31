# Lipogram
## 문제
리포그램(lipogram)은 팬그램(pangram)과 반대되는 개념으로, 알파벳의 일부 글자를 사용하지 않고 만든 문장이다. 주어진 문자열이 리포그램인지 확인해보자.

## 입력
첫째 줄에 알파벳 소문자로 이루어진 문자열 S (1 ≤ |S| ≤ 100) 가 주어진다. S 는 공백 또는 알파벳 대소문자로 이루어진 문자열이다.

## 출력
주어진 문자열 S 가 리포그램이라면 YES 를 출력하고 두 번째 줄에 사용하지 않은 알파벳을 출력한다. 사용하지 않은 알파벳은 소문자로 출력하며, 알파벳 순서대로 출력한다.

리포그램이 아니라면 NO 를 출력한다.

## 예제 입력 1
```
The Quick Brown Fox Jumps Over The Lazy Dog
```
## 예제 출력 1
```
NO
```
## 예제 입력 2
```
Bubble sort Quick sort Merge sort prefix sum Binary search Fibonacci Dijkstra
```
## 예제 출력 2
```
YES
vwz
```
## 예제 입력 3
```
AbCdEfGhIjKlMnOpQrStUvWxYz
```
## 예제 출력 3
```
NO
```
