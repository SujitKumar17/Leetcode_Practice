#include <stdlib.h>
#include <string.h>

char* longestPalindrome(char* s) {
    int n = (int)strlen(s);
    int start = 0;
    int maxLen = 1;

    for (int i = 0; i < n; i++) {
        /* Two passes per index: odd-length (i, i) and even-length (i, i+1) */
        for (int pass = 0; pass < 2; pass++) {
            int left = i;
            int right = i + pass;

            while (left >= 0 && right < n && s[left] == s[right]) {
                left--;
                right++;
            }

            /* After the loop, the palindrome spans (left+1) to (right-1) */
            int len = right - left - 1;
            if (len > maxLen) {
                maxLen = len;
                start = left + 1;
            }
        }
    }

    char* result = (char*)malloc((size_t)maxLen + 1);
    memcpy(result, s + start, (size_t)maxLen);
    result[maxLen] = '\0';
    return result;
}