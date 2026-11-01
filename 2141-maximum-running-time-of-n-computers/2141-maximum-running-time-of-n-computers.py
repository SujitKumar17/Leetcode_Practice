class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        total = sum(batteries)

        while batteries[-1] > total // n:
            total -= batteries.pop()
            n -= 1

        return total // n
