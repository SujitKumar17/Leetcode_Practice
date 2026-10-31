class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        R = [[0] * (n + 1) for _ in range(m + 1)]
        D = [[0] * (n + 1) for _ in range(m + 1)]

        R[0][0] = 1

        for i in range(m):
            for j in range(n):
                r, d = R[i][j], D[i][j]
                if r == 0 and d == 0:
                    continue

                if grid[i][j] == 0:
                    total = (r + d) % MOD
                    if i == m - 1 and j == n - 1:
                        return total
                    # move right
                    if j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + total) % MOD
                    # move down
                    if i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + total) % MOD
                else:
                 
                    if r and i + 1 < m:
                        D[i + 1][j] = (D[i + 1][j] + r) % MOD
                 
                    if d and j + 1 < n:
                        R[i][j + 1] = (R[i][j + 1] + d) % MOD

        return 0