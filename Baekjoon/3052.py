arr = []

for i in range(10):
    n = int(input()) #n 입력
    arr.append(n % 42)  #42 나머지 arr 저장
arr = set(arr) # 집합 자료형
print(len(arr)) # arr의 길이
