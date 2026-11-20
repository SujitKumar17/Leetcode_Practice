from collections import defaultdict


class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = defaultdict(int)
        ans = 0
        for x in nums:
            # Handle x + 1 first so one element isn't used for both x and x + 1
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1
            ans = max(ans, dp[x], dp[x + 1])
        return ans