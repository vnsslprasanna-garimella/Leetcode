class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n=len(classroom), len(classroom[0])
        l_map={}
        sx, sy=0, 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    sx, sy=i, j
                elif classroom[i][j]=='L':
                    l_map[(i, j)]=len(l_map)
        target=(1<<len(l_map))-1
        if target==0:
            return 0
        visited={}
        q=collections.deque([(sx, sy, 0, energy, 0)])
        visited[(sx, sy, 0)]=energy
        while q:
            r, c, mask, e, d=q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc=r+dr, c+dc
                if 0<=nr<m and 0<=nc<n and classroom[nr][nc]!='X':
                    ne=e-1
                    if ne<0:
                        continue
                    nmask=mask
                    cell=classroom[nr][nc]
                    if cell=='L':
                        nmask|=(1<<l_map[(nr, nc)])
                    elif cell=='R':
                        ne=energy
                    if nmask==target:
                        return d+1
                    if ne>0 or cell=='R':
                        if visited.get((nr, nc, nmask), -1)<ne:
                            visited[(nr, nc, nmask)]=ne
                            q.append((nr, nc, nmask, ne, d+1))
        return -1