
 #PriorityQueue - thread-safe로 사용X
from queue import PriorityQueue

pq = PriorityQueue()
pq.put(6)
pq.put(10)
pq.put(-5)
pq.put(0)
pq.put(8)
while not pq.empty():
  print(pq.get())  #pop과 같은 역할


#따라서, heapq 사용. (PriorityQueue 대신)
import heapq 

pq = []
heapq.heappush(pq, 6)
heapq.heappush(pq, 12)
heapq.heappush(pq, 0)
heapq.heappush(pq, -5)
heapq.heappush(pq, 8)
print(pq)
while pq: 
  print(pq[0]) # 최상단 노드를 알고 싶을 떄
  heapq.heappop(pq)


#hq로 요약해서 사용 가능. 
import heapq as hq

pq = []
hq.heappush(pq, 6)
hq.heappush(pq, 12)
hq.heappush(pq, 0)
hq.heappush(pq, -5)
hq.heappush(pq, 8)
print(pq)
while pq: 
  print(pq[0]) 
  hq.heappop(pq)


## heapq - python
#import heapq

#pq = []
#heapq.heappush(pq, 456)
#heapq.heappush(pq, 123)
#heapq.heappush(pq, 789)
#print("size:", len(pq))
#while len(pq) > 0:
# print(heapq.heappop(pq))
  
  
 