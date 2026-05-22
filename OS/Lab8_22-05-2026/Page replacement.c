#include <stdio.h>
#include <limits.h>

void fifo(int p[], int n, int c) {
    int f[10], i, j, fault = 0, k = 0, found;
    for (i = 0; i < c; i++) f[i] = -1;

    printf("\n--- FIFO ---\n");
    for (i = 0; i < n; i++) {
        found = 0;
        for (j = 0; j < c; j++) {
            if (f[j] == p[i]) { found = 1; break; }
        }
        if (!found) {
            f[k] = p[i];
            k = (k + 1) % c;
            fault++;
        }
        printf("P%d: ", p[i]);
        for (j = 0; j < c; j++) (f[j] != -1) ? printf("%d ", f[j]) : printf("- ");
        printf("\n");
    }
    printf("Total Faults: %d\n", fault);
}

void lru(int p[], int n, int c) {
    int f[10], time[10], i, j, fault = 0, found, min, lru_idx;
    for (i = 0; i < c; i++) f[i] = -1;

    printf("\n--- LRU ---\n");
    for (i = 0; i < n; i++) {
        found = 0;
        for (j = 0; j < c; j++) {
            if (f[j] == p[i]) {
                found = 1;
                time[j] = i; 
                break;
            }
        }
        if (!found) {
            int empty = -1;
            for (j = 0; j < c; j++) if (f[j] == -1) { empty = j; break; }

            if (empty != -1) {
                f[empty] = p[i];
                time[empty] = i;
            } else {
                min = time[0]; lru_idx = 0;
                for (j = 1; j < c; j++) {
                    if (time[j] < min) { min = time[j]; lru_idx = j; }
                }
                f[lru_idx] = p[i];
                time[lru_idx] = i;
            }
            fault++;
        }
        printf("P%d: ", p[i]);
        for (j = 0; j < c; j++) (f[j] != -1) ? printf("%d ", f[j]) : printf("- ");
        printf("\n");
    }
    printf("Total Faults: %d\n", fault);
}

void optimal(int p[], int n, int c) {
    int f[10], i, j, k, fault = 0, found;
    for (i = 0; i < c; i++) f[i] = -1;

    printf("\n--- Optimal ---\n");
    for (i = 0; i < n; i++) {
        found = 0;
        for (j = 0; j < c; j++) {
            if (f[j] == p[i]) { found = 1; break; }
        }
        if (!found) {
            int empty = -1;
            for (j = 0; j < c; j++) if (f[j] == -1) { empty = j; break; }

            if (empty != -1) f[empty] = p[i];
            else {
                int max = -1, opt_idx = 0;
                for (j = 0; j < c; j++) {
                    int next_use = INT_MAX;
                    for (k = i + 1; k < n; k++) {
                        if (f[j] == p[k]) { next_use = k; break; }
                    }
                    if (next_use > max) { max = next_use; opt_idx = j; }
                }
                f[opt_idx] = p[i];
            }
            fault++;
        }
        printf("P%d: ", p[i]);
        for (j = 0; j < c; j++) (f[j] != -1) ? printf("%d ", f[j]) : printf("- ");
        printf("\n");
    }
    printf("Total Faults: %d\n", fault);
}

int main() {
    int n, c, i;
    int p[30];

    printf("Enter number of pages: "); scanf("%d", &n);
    printf("Enter reference string: ");
    for (i = 0; i < n; i++) scanf("%d", &p[i]);
    printf("Enter number of frames: "); scanf("%d", &c);

    fifo(p, n, c);
    lru(p, n, c);
    optimal(p, n, c);

    return 0;
}
/* Output:
Enter number of pages: 10
Enter reference string: 7 0 1 2 0 3 0 4 2 3
Enter number of frames: 3

--- FIFO ---
P7: 7 - - 
P0: 7 0 - 
P1: 7 0 1 
P2: 2 0 1 
P0: 2 0 1 
P3: 2 3 1 
P0: 2 3 0 
P4: 4 3 0 
P2: 4 2 0 
P3: 4 2 3 
Total Faults: 9
...
*/
