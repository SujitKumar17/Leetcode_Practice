class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        # Step 1: multi-source BFS gives each cell's distance to the nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < n and 0 <= y < n and dist[x][y] == -1:
                    dist[x][y] = dist[r][c] + 1
                    q.append((x, y))

        # Step 2: always expand the safest reachable cell first (max-heap)
        heap = [(-dist[0][0], 0, 0)]
        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        while heap:
            d, r, c = heapq.heappop(heap)
            safe = -d

            if r == n - 1 and c == n - 1:
                return safe

            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < n and 0 <= y < n and not seen[x][y]:
                    seen[x][y] = True
                    heapq.heappush(heap, (-min(safe, dist[x][y]), x, y))

        return 0