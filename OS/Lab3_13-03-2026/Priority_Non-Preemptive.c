#include <stdio.h>

int main() {
    int n, i, j, cur_time = 0, count = 0;
    int at[10], bt[10], pri[10], ct[10], tat[10], wt[10], finished[10] = {0};
    float total_wt = 0, total_tat = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        printf("P%d AT, BT, Priority: ", i + 1);
        scanf("%d %d %d", &at[i], &bt[i], &pri[i]);
    }

    while(count < n) {
        int idx = -1, min_pri = 999;
        for(i = 0; i < n; i++) {
            if(at[i] <= cur_time && !finished[i] && pri[i] < min_pri) {
                min_pri = pri[i];
                idx = i;
            }
        }

        if(idx != -1) {
            cur_time += bt[idx];
            ct[idx] = cur_time;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];
            finished[idx] = 1;
            count++;
            total_tat += tat[idx];
            total_wt += wt[idx];
        } else cur_time++;
    }

    printf("\nP\tAT\tBT\tPri\tCT\tTAT\tWT\n");
    for(i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\t%d\t%d\t%d\n", i+1, at[i], bt[i], pri[i], ct[i], tat[i], wt[i]);
    
    printf("\nAvg TAT: %.2f\nAvg WT: %.2f\n", total_tat/n, total_wt/n);
    return 0;
}
