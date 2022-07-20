from collections import deque
dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    s[i][j] = "*"
    while q:
        a, b = q.popleft()
        for k in range(8):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < m and 0 <= y < n and s[x][y] == "@":
                s[x][y] = "*"
                q.append([x, y])
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    s = []
    for i in range(m):
        s.append(list(input()))
    cnt = 0
    for i in range(m):
        for j in range(n):
            if s[i][j] == "@":
                bfs(i, j)
                cnt += 1
    print(cnt)