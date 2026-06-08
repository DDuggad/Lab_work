#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int knapSack(int W, int wt[], int val[], int n) {
    int i, w;
    int dp[n + 1][W + 1];

    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (wt[i - 1] <= w)
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }
    return dp[n][W];
}

int main() {
    int n, W, i;
    int val[20], wt[20];

    printf("Enter number of items: ");
    scanf("%d", &n);

    printf("Enter values: ");
    for (i = 0; i < n; i++) scanf("%d", &val[i]);

    printf("Enter weights: ");
    for (i = 0; i < n; i++) scanf("%d", &wt[i]);

    printf("Enter knapsack capacity: ");
    scanf("%d", &W);

    printf("\nMaximum Profit: %d\n", knapSack(W, wt, val, n));
    
    return 0;
}
/* Output:
Enter number of items: 3
Enter values: 60 100 120
Enter weights: 10 20 30
Enter knapsack capacity: 50

Maximum Profit: 220
*/
