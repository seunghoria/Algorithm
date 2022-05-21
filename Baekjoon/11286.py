import heapq as hq
import sys

input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq,(abs(x), x)) # 튜플 (절대값, 원본값) - 우선순위 큐에 저장

    else: # x = 0
      print(hq.heappop(pq)[1] if pq else 0)