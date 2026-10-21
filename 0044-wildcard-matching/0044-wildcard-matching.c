bool isMatch(char *s, char *p) {
    char *star = NULL;
    char *ss = s;

    while (*s) {
        if (*p == '?' || *p == *s) {
            s++;
            p++;
        } else if (*p == '*') {
            star = p;
            ss = s;
            p++;
        } else if (star) {
            p = star + 1;
            ss++;
            s = ss;
        } else {
            return false;
        }
    }

    while (*p == '*') {
        p++;
    }

    return *p == '\0';
}