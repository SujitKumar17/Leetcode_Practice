#include <stdlib.h>

#define MAX_SIZE 40005

typedef struct {
    int prefix[MAX_SIZE];
    int size;   // number of entries in prefix (prefix[0] = 1 is a sentinel)
} ProductOfNumbers;

ProductOfNumbers* productOfNumbersCreate() {
    ProductOfNumbers* obj = (ProductOfNumbers*)malloc(sizeof(ProductOfNumbers));
    obj->prefix[0] = 1;
    obj->size = 1;
    return obj;
}

void productOfNumbersAdd(ProductOfNumbers* obj, int num) {
    if (num == 0) {
        // Any window containing this zero has product 0, so reset.
        obj->prefix[0] = 1;
        obj->size = 1;
    } else {
        obj->prefix[obj->size] = obj->prefix[obj->size - 1] * num;
        obj->size++;
    }
}

int productOfNumbersGetProduct(ProductOfNumbers* obj, int k) {
    // Only size-1 numbers exist since the last zero.
    // If k reaches back past (or onto) that zero, the product is 0.
    if (k >= obj->size) {
        return 0;
    }
    return obj->prefix[obj->size - 1] / obj->prefix[obj->size - 1 - k];
}

void productOfNumbersFree(ProductOfNumbers* obj) {
    free(obj);
}
