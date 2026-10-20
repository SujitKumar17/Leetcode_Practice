#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    int n = (int)strlen(s);

    /* Edge case: no zigzag possible */
    if (numRows == 1 || numRows >= n) {
        char* res = (char*)malloc(n + 1);
        if (res == NULL) return NULL;
        strcpy(res, s);
        return res;
    }

    /* One buffer per row, each large enough to hold the whole string */
    char** rows = (char**)malloc(numRows * sizeof(char*));
    int* len = (int*)calloc(numRows, sizeof(int));
    if (rows == NULL || len == NULL) {
        free(rows);
        free(len);
        return NULL;
    }
    for (int i = 0; i < numRows; i++) {
        rows[i] = (char*)malloc(n + 1);
        if (rows[i] == NULL) {
            for (int j = 0; j < i; j++) free(rows[j]);
            free(rows);
            free(len);
            return NULL;
        }
    }

    /* Distribute characters zigzag-style */
    int curRow = 0;
    int step = 1; /* +1 going down, -1 going up */
    for (int i = 0; i < n; i++) {
        rows[curRow][len[curRow]++] = s[i];
        if (curRow == 0) step = 1;
        else if (curRow == numRows - 1) step = -1;
        curRow += step;
    }

    /* Concatenate rows into the result */
    char* result = (char*)malloc(n + 1);
    if (result == NULL) {
        for (int i = 0; i < numRows; i++) free(rows[i]);
        free(rows);
        free(len);
        return NULL;
    }
    int pos = 0;
    for (int i = 0; i < numRows; i++) {
        memcpy(result + pos, rows[i], len[i]);
        pos += len[i];
        free(rows[i]);
    }
    result[pos] = '\0';

    free(rows);
    free(len);
    return result;
}