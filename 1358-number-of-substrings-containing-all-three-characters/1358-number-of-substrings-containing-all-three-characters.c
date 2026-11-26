int numberOfSubstrings(char* s) {
    int last[3] = {-1, -1, -1};
    int count = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        last[s[i] - 'a'] = i;

        int minIndex = last[0];
        if (last[1] < minIndex) minIndex = last[1];
        if (last[2] < minIndex) minIndex = last[2];

        count += minIndex + 1;
    }

    return count;
}