# http://baozitraining.org/blog/google%E6%9C%80%E6%96%B0%E9%9D%A2%E8%AF%95%E9%A2%98-continental-divider/

def reachable(i, j, ni, nj, mat):
    if ni < 0 or ni >= len(mat) or nj < 0 or nj >= len(mat[0]):
        return False
    if mat[ni][nj] < mat[i][j]:
        return False
    return True


def Continental_divider(mat):
    def bfs(i, j):
        if (i, j) in visited:
            return 
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        p[idx].add((i, j))
        visited.add((i, j))
        for d in DIRS:
            ni, nj = i + d[0], j + d[1]
            if reachable(i, j, ni, nj, mat):
                bfs(ni, nj)
        visited.remove((i, j))

    sea, maxh = 0, 0 
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                sea += 1
            maxh = max(maxh, mat[i][j])
    p = [set() for i in range(sea)]
    idx = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                visited = set()
                bfs(i, j)
                idx += 1
    res = p[0]
    for i in range(1, len(p)):
        res &= p[i]
    return res




def Pac_Alt(land):
    n = len(land)
    if n < 1:
        return None

    def dfs(p, visited, land):
        DIRS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for d in DIRS:
            nx, ny = p.x + d[0], p.y + d[1]
            newp = Point(nx, ny)
            if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land):
                continue
            if land[nx][ny] < land[x][y] or newp in visited:
                continue
            visited.add(newp
            dfs(newp, visited, land)
            
                    
    pac = set()
    for i in range(n):
        p = Point(0, i)
        pac.add(p)
        dfs(p, pac, land)
        
    for i in range(n):
        p = Point(i, 0)
        pac.add(p)
        dfs(p, pac, land)

    alt = set()
    for i in range(n):
        p = Point(n-1, i)
        alt.add(p)
        dfs(p, alt, land)
        
    for i in range(n):
        p = Point(i, n-1)
        pac.add(p)
        dfs(p, alt, land)
    return pac&alt
            

mat = [[0, 1, 2, 0],
       [4, 3, 3, 1],
       [0, 2, 0, 2]]



print Continental_divider(mat)

        
            
        
