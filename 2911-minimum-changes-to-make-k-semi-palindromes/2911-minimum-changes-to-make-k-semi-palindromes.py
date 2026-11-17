class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float("inf")

        # Proper divisors of each length (d < length)
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)

        # cost[i][j] = min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                best = INF
                for d in divisors[L]:
                    m = L // d              # elements per group
                    changes = 0
                    for r in range(d):
                        lo = i + r
                        hi = i + r + (m - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                changes += 1
                            lo += d
                            hi -= d
                    if changes < best:
                        best = changes
                cost[i][j] = best

        # dp[p][i] = min cost to split first i chars into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):   # last part s[j:i], length >= 2
                    if dp[p - 1][j] != INF and cost[j][i - 1] != INF:
                        val = dp[p - 1][j] + cost[j][i - 1]
                        if val < dp[p][i]:
                            dp[p][i] = val

        return dp[k][n]


# Quick checks
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumChanges("abcac", 2))    # 1
    print(sol.minimumChanges("abcdef", 2))   # 2
    print(sol.minimumChanges("aabbaa", 3))   # 0