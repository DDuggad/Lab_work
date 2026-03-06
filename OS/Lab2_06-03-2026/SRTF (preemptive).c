#include <stdio.h>

int main() {
    int n, time = 0, comp = 0, at[10], bt[10], rt[10], ct[10], tat[10], wt[10];
    float avg_wt = 0, avg_tat = 0;

    printf("Enter no of processes: "); 
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        printf("Enter AT and BT for P%d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        rt[i] = bt[i]; 
    }

    while (comp < n) {
        int idx = -1, min_rt = 1e9;
        for (int i = 0; i < n; i++) {
            if (at[i] <= time && rt[i] > 0 && rt[i] < min_rt) {
                min_rt = rt[i];
                idx = i;
            }
        }
        
        if (idx != -1) {
            rt[idx]--;
            time++;
            if (rt[idx] == 0) {
                ct[idx] = time;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];
                avg_wt += wt[idx]; 
                avg_tat += tat[idx];
                comp++;
            }
        } else {time++;}
    }
    printf("\nP\tAT\tBT\tCT\tTAT\tWT\n");
    for (int i = 0; i < n; i++) printf("P%d\t%d\t%d\t%d\t%d\t%d\n", i + 1, at[i], bt[i], ct[i], tat[i], wt[i]);
    printf("\nAvg WT: %.2f\nAvg TAT: %.2f\n", avg_wt / n, avg_tat / n);
    return 0;
}
