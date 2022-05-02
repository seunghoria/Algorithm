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

q = deque()
q.append(123)
q.append(456)
q.append(789)
print("size:", len(q))
while len(q) > 0:
  print(q.popleft())