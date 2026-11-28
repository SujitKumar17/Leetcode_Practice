class Solution(object):
    def maximumSaleItems(self, items, budget):
        """
        :type items: List[List[int]]
        :type budget: int
        :rtype: int
        """
        n = len(items)

        # freq[f] = number of items with factor f
        freq = [0] * (n + 1)
        for factor, _ in items:
            freq[factor] += 1

        # multiples[f] = number of items whose factor is divisible by f
        multiples = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f]:
                multiples[f] = sum(freq[f::f])

        min_price = min(price for _, price in items)

        # (price, number of bonus copies), only where worthwhile
        deals = []
        for factor, price in items:
            count = multiples[factor] - 1  # exclude the item itself
            if count > 0 and price < 2 * min_price:
                deals.append((price, count))

        deals.sort()

        result = 0
        for price, count in deals:
            take = min(count, budget // price)
            if take == 0:
                break
            result += 2 * take
            budget -= take * price

        # Spend what is left on the cheapest item
        result += budget // min_price

        return result