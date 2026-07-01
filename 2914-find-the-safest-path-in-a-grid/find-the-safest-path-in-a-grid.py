from collections import deque
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Find distance of every cell from the nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Add all thief cells to the queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Multi-source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Check if a path exists with minimum safeness >= value
        def can_reach(safe):
            if dist[0][0] < safe:
                return False

            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True

            while q:
                r, c = q.popleft()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < n and 0 <= nc < n and
                        not visited[nr][nc] and
                        dist[nr][nc] >= safe):

                        visited[nr][nc] = True
                        q.append((nr, nc))

            return False

        # Step 3: Binary Search on the answer
        left, right = 0, 2 * n
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans