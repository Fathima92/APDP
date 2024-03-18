from collections import deque

q = deque()

q.append('1st Element')
q.append('2nd Element')
q.append('3rd Element')
print(q, '\n')

a = q.popleft()
print(a)
b = q.popleft()
print(b)
c = q.popleft()
print(c)
