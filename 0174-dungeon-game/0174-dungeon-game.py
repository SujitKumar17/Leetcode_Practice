class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        INF = float('inf')

        dp = [INF] * (n + 1)
        dp[n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(1, need)
            dp[n] = INF

        return dp[0]