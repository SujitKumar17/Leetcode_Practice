#include <stdlib.h>

int* findSubtreeSizes(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    int *head   = malloc(n * sizeof(int));
    int *nxt    = malloc(n * sizeof(int));
    int *it     = malloc(n * sizeof(int));
    int *stack  = malloc(n * sizeof(int));
    int *saved  = malloc(n * sizeof(int));
    int *newp   = malloc(n * sizeof(int));
    int *order  = malloc(n * sizeof(int));
    int *ans    = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) { head[i] = -1; nxt[i] = -1; }
    for (int i = 1; i < n; i++) {
        nxt[i] = head[parent[i]];
        head[parent[i]] = i;
    }
    for (int i = 0; i < n; i++) it[i] = head[i];

    int last[26];
    for (int i = 0; i < 26; i++) last[i] = -1;

    int sp = 0, cnt = 0;

    // enter root
    int c = s[0] - 'a';
    saved[0] = last[c];
    newp[0] = -1;
    last[c] = 0;
    order[cnt++] = 0;
    stack[sp++] = 0;

    // iterative DFS on the ORIGINAL tree
    while (sp > 0) {
        int u = stack[sp - 1];
        if (it[u] != -1) {
            int v = it[u];
            it[u] = nxt[v];
            c = s[v] - 'a';
            newp[v] = (last[c] != -1) ? last[c] : parent[v];
            saved[v] = last[c];
            last[c] = v;
            order[cnt++] = v;
            stack[sp++] = v;
        } else {
            last[s[u] - 'a'] = saved[u];
            sp--;
        }
    }

    for (int i = 0; i < n; i++) ans[i] = 1;

    // new parent is always an ancestor in the original tree, so it appears
    // earlier in preorder; reverse preorder accumulates sizes correctly
    for (int i = cnt - 1; i >= 1; i--) {
        int x = order[i];
        ans[newp[x]] += ans[x];
    }

    free(head); free(nxt); free(it); free(stack);
    free(saved); free(newp); free(order);

    *returnSize = n;
    return ans;
}