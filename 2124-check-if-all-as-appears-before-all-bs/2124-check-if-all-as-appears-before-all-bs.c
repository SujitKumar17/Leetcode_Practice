bool checkString(char* s) {
    bool seenB = false;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'b') {
            seenB = true;
        } else if (seenB) {
            return false;
        }
    }
    return true;
    
}