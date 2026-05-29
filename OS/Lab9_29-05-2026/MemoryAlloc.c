
#include <stdio.h>

void firstFit(int b[], int nb, int p[], int np) {
    int alloc[10], temp_b[10], i, j;
    for (i = 0; i < nb; i++) temp_b[i] = b[i];
    for (i = 0; i < np; i++) alloc[i] = -1;

    for (i = 0; i < np; i++) {
        for (j = 0; j < nb; j++) {
            if (temp_b[j] >= p[i]) {
                alloc[i] = j;
                temp_b[j] -= p[i];
                break;
            }
        }
    }
    printf("\nFirst-Fit Allocation:\n");
    for (i = 0; i < np; i++) {
        if (alloc[i] != -1) printf("P%d (Size: %d) -> Block %d\n", i + 1, p[i], alloc[i] + 1);
        else printf("P%d (Size: %d) -> Not Allocated\n", i + 1, p[i]);
    }
}

void bestFit(int b[], int nb, int p[], int np) {
    int alloc[10], temp_b[10], i, j;
    for (i = 0; i < nb; i++) temp_b[i] = b[i];
    for (i = 0; i < np; i++) alloc[i] = -1;

    for (i = 0; i < np; i++) {
        int best = -1;
        for (j = 0; j < nb; j++) {
            if (temp_b[j] >= p[i]) {
                if (best == -1 || temp_b[j] < temp_b[best]) best = j;
            }
        }
        if (best != -1) {
            alloc[i] = best;
            temp_b[best] -= p[i];
        }
    }
    printf("\nBest-Fit Allocation:\n");
    for (i = 0; i < np; i++) {
        if (alloc[i] != -1) printf("P%d (Size: %d) -> Block %d\n", i + 1, p[i], alloc[i] + 1);
        else printf("P%d (Size: %d) -> Not Allocated\n", i + 1, p[i]);
    }
}

void worstFit(int b[], int nb, int p[], int np) {
    int alloc[10], temp_b[10], i, j;
    for (i = 0; i < nb; i++) temp_b[i] = b[i];
    for (i = 0; i < np; i++) alloc[i] = -1;

    for (i = 0; i < np; i++) {
        int worst = -1;
        for (j = 0; j < nb; j++) {
            if (temp_b[j] >= p[i]) {
                if (worst == -1 || temp_b[j] > temp_b[worst]) worst = j;
            }
        }
        if (worst != -1) {
            alloc[i] = worst;
            temp_b[worst] -= p[i];
        }
    }
    printf("\nWorst-Fit Allocation:\n");
    for (i = 0; i < np; i++) {
        if (alloc[i] != -1) printf("P%d (Size: %d) -> Block %d\n", i + 1, p[i], alloc[i] + 1);
        else printf("P%d (Size: %d) -> Not Allocated\n", i + 1, p[i]);
    }
}

int main() {
    int b[10], p[10], nb, np, i, ch;

    printf("Enter number of memory blocks: "); scanf("%d", &nb);
    printf("Enter size of each block:\n");
    for (i = 0; i < nb; i++) { printf("Block %d: ", i + 1); scanf("%d", &b[i]); }

    printf("Enter number of processes: "); scanf("%d", &np);
    printf("Enter size of each process:\n");
    for (i = 0; i < np; i++) { printf("Process %d: ", i + 1); scanf("%d", &p[i]); }

    while (1) {
        printf("\nMenu: 1.First Fit  2.Best Fit  3.Worst Fit  4.Exit\nEnter choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1: firstFit(b, nb, p, np); break;
            case 2: bestFit(b, nb, p, np); break;
            case 3: worstFit(b, nb, p, np); break;
            case 4: return 0;
            default: printf("Invalid choice!\n");
        }
    }
    return 0;
}