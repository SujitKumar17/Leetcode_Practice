class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Only overflow case: -2^31 / -1 = 2^31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        quotient = 0
        # Subtract the largest shifted divisor (b << k) that still fits in a
        for k in range(31, -1, -1):
            if (b << k) <= a:
                a -= b << k
                quotient += 1 << k

        return -quotient if negative else quotient


if __name__ == "__main__":
    s = Solution()
    assert s.divide(10, 3) == 3
    assert s.divide(7, -3) == -2
    assert s.divide(-7, 3) == -2
    assert s.divide(-7, -3) == 2
    assert s.divide(0, 5) == 0
    assert s.divide(1, 1) == 1
    assert s.divide(1, 2) == 0
    assert s.divide(-1, 1) == -1
    assert s.divide(-2**31, -1) == 2**31 - 1
    assert s.divide(-2**31, 1) == -2**31
    assert s.divide(2**31 - 1, 1) == 2**31 - 1
    assert s.divide(-2**31, 2) == -2**30
    assert s.divide(-2**31, -2**31) == 1
    assert s.divide(2**31 - 1, -2**31) == 0
    print("All tests passed")