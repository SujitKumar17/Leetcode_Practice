class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        lo, hi = min(need1, need2), max(need1, need2)
        # Cost of covering the larger need with a single-type item
        cost_hi = cost1 if need1 > need2 else cost2

        # Option 1: buy only single-type items
        option1 = need1 * cost1 + need2 * cost2

        # Option 2: buy `lo` type-3 items, then cover the remaining need
        # with whichever is cheaper: single-type items or more type-3 items
        option2 = lo * costBoth + (hi - lo) * min(cost_hi, costBoth)

        # Option 3: buy `hi` type-3 items, which covers both needs
        option3 = hi * costBoth

        return min(option1, option2, option3)