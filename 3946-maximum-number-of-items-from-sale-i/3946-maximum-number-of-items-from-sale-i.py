class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        LIMIT = 1500

        # Count how many items have each factor
        freq = [0] * (LIMIT + 1)
        for factor, _ in items:
            freq[factor] += 1

        # bonus[f] = free copies from first purchase of an item with factor f
        # (subtract 1 to exclude the item itself)
        bonus = {f: sum(freq[f::f]) - 1 for f in {f for f, _ in items}}

        # 0/1 knapsack over the FIRST copy of each item
        dp = [0] * (budget + 1)
        for factor, price in items:
            value = 1 + bonus[factor]
            for cost in range(budget, price - 1, -1):
                if dp[cost - price] + value > dp[cost]:
                    dp[cost] = dp[cost - price] + value

        # Spend leftover money on extra copies of the cheapest item
        cheapest = min(price for _, price in items)

        return max(dp[c] + (budget - c) // cheapest for c in range(budget + 1))