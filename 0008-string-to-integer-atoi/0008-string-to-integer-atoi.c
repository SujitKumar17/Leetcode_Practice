int myAtoi(char *s) {
    int i = 0;
    int sign = 1;
    long long result = 0;

    // 1. Skip leading whitespace
    while (s[i] == ' ') {
        i++;
    }

    // 2. Read optional sign
    if (s[i] == '-') {
        sign = -1;
        i++;
    } else if (s[i] == '+') {
        i++;
    }

    // 3. Read digits and clamp on overflow
    while (s[i] >= '0' && s[i] <= '9') {
        result = result * 10 + (s[i] - '0');

        if (sign == 1 && result > 2147483647LL) {
            return 2147483647;
        }
        if (sign == -1 && -result < -2147483648LL) {
            return -2147483648;
        }
        i++;
    }

    return (int)(sign * result);
}