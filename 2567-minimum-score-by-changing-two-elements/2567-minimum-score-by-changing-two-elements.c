#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (x > y) - (x < y);
}

int minimizeSum(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), cmp);

    int a = nums[numsSize - 1] - nums[2];   // change two smallest
    int b = nums[numsSize - 2] - nums[1];   // change smallest and largest
    int c = nums[numsSize - 3] - nums[0];   // change two largest

    int ans = a;
    if (b < ans) ans = b;
    if (c < ans) ans = c;
    return ans;
}