#include <stdio.h>

void knapsack(int n, float w[], float v[], float cap) {
    float x[10] = {0}, total = 0;
    int i, j;
    float ratio[10];

    for (i = 0; i < n; i++) ratio[i] = v[i] / w[i];

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (ratio[i] < ratio[j]) {
                float t = ratio[i]; ratio[i] = ratio[j]; ratio[j] = t;
                t = w[i]; w[i] = w[j]; w[j] = t;
                t = v[i]; v[i] = v[j]; v[j] = t;
            }
        }
    }

    for (i = 0; i < n; i++) {
        if (w[i] > cap) break;
        x[i] = 1.0;
        total += v[i];
        cap -= w[i];
    }
    if (i < n) {
        x[i] = cap / w[i];
        total += x[i] * v[i];
    }

    printf("\nTotal Profit: %.2f\n", total);
}

int main() {
    int n, i;
    float w[10], v[10], cap;
    printf("Enter n: "); scanf("%d", &n);
    printf("Enter Weights: "); for (i = 0; i < n; i++) scanf("%f", &w[i]);
    printf("Enter Values: "); for (i = 0; i < n; i++) scanf("%f", &v[i]);
    printf("Enter Capacity: "); scanf("%f", &cap);
    knapsack(n, w, v, cap);
    return 0;
}
/* Output:
Enter n: 3
Enter Weights: 10 20 30
Enter Values: 60 100 120
Enter Capacity: 50
Total Profit: 240.00
*/
