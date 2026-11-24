class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        best = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                prod *= x
                g = gcd(g, x)
                l = l * x // gcd(l, x)

                if prod == l * g:
                    best = max(best, j - i + 1)

        return best