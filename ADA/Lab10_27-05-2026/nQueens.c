
#include <stdio.h>
#include <stdlib.h>

int x[20], count = 0;

int place(int k, int i) {
    for (int j = 1; j < k; j++) {
        if (x[j] == i || abs(x[j] - i) == abs(j - k)) 
            return 0;
    }
    return 1;
}

void nQueens(int k, int n) {
    for (int i = 1; i <= n; i++) {
        if (place(k, i)) {
            x[k] = i;
            if (k == n) {
                printf("\nSolution %d: ", ++count);
                for (int j = 1; j <= n; j++) printf("%d ", x[j]);
            } else {
                nQueens(k + 1, n);
            }
        }
    }
}

int main() {
    int n;
    printf("Enter number of queens: ");
    scanf("%d", &n);

    if (n == 2 || n == 3) {
        printf("No solution exists for N=%d\n", n);
    } else {
        nQueens(1, n);
        printf("\n\nTotal Solutions: %d\n", count);
    }
    return 0;
}