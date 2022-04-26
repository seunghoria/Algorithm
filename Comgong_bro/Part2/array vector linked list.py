#1) 배열 Array
arr = [10, 11, 12, 13]
arr[2] = 5
##- 삽입/삭제' 시간복잡도 : O(N)
##- 탐색 : O(1) 
##=> 탐색이 더 시간 복잡도가 빠르다.
##-Python은 리스트를 사용



#2) 벡터 Vector
#:  c++ 유저를 위해 준비함
v = []
v.append((123, 456))
v.append((789, 987))
print("size:", len(v))
for p in v:
	print(p)
##파이썬은 list를 쓰면 원래 사이즈가 변경가능하기 때문에 list를 쓰고, 
##pair처럼 2개의 값을 저장하기 위해서는 튜플(?)을 사용할 수 있다.
##물론, 리스트를 사용할 수도 있는데 여기서는 튜플을 사용해 보았다.



#3) 연결 리스트 Linked List
#c++에서는 기본 stl로 오른쪽 코드처럼 제공.