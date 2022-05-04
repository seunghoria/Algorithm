# 1. 스택 Stack
s = []
s.append(123)
s.append(456)
s.append(789)
print("size:", len(s))
while len(s) > 0:
  print(s[-1])
  s.pop(-1)


# 2. 큐 Queue

from collections import deque

dq = deque()
dq.append(123)
dq.appendleft(456)
dq.appendleft(789)
print(dq)

print(dq.pop())
print(dq.popleft())

dq [789, 456, 123]

from queue import Queue
# 이 모듈은 멀티 스레드 환경을 위한 "thread-safe"기능으로
# 실제 속도가 느려 쓸 필요가 없다. - 시간 초과 발생.
q = Queue()
q.put(123)
q.put(456)
q.put(789)
while q:
  print(q.get())
  
  
  