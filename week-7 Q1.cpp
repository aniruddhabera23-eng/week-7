#include <stdio.h>

void printNto1(int n) {
    if (n == 0) {
        return; // base case: stop recursion when n reaches 0
    }
    printf("%d\n", n);
    printNto1(n - 1); // recursive call with n-1
}

int main() {
    int N = 5;
    printNto1(N);
    return 0;
}
