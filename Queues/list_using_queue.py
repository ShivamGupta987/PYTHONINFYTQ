from collections import deque

a = deque()

a.append(4)
a.append(8)
print(a)

a.popleft()
print(a)
a.popleft()
print(a)