## input
n = input() 
# input이라는 함수는 표준 입력을 받아서 한 줄에 string을 받아서 반환해주는 함수
# input 무조건 문자열 반환

n = int(input())  #정수 반환
print(n + 4)

n = input().split() #각각의 원소를 갖는 리스트 반환
print(n)

# map 함수 사용 - 각각 요소들에 내가 원하는 효과 적용 가능.
a, b = map(int, input().split())
print(a + 3)
print(b + 4)

a,b,c = map(int, input().split())
print(a,b,c)

## 빠른 입출력 함수
for _ in range(100000):
  n = int(input())
  print(n)

#import sys

for _ in range(100000):
    n = int(sys.stdin.readline())
    print(n)


# 빠른 입출력 함수 실습 _ baekjoon _ 15552
import sys
case = int(sys.stdin.readline())

for _ in range(case):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)