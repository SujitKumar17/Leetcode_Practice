#include <stdbool.h>

bool canAliceWin(int n) {
    int stones = 10;
    bool aliceWins = false;

    while (stones > 0 && n >= stones) {
        n -= stones;
        stones--;
        aliceWins = !aliceWins;
    }

    return aliceWins;
}