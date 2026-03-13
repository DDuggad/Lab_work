#include <stdio.h>

int main() {
    int n, i, cur_time = 0, count = 0;
    int at[10], bt[10], temp[10], pri[10], ct[10], tat[10], wt[10];
    float total_wt = 0, total_tat = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++) {
        printf("P%d AT, BT, Priority: ", i + 1);
        scanf("%d %d %d", &at[i], &bt[i], &pri[i]);
        temp[i] = bt[i];
    }

    while(count < n) {
        int idx = -1, min_pri = 999;
        for(i = 0; i < n; i++) {
            if(at[i] <= cur_time && temp[i] > 0 && pri[i] < min_pri) {
                min_pri = pri[i];
                idx = i;
            }
        }

        if(idx != -1) {
            temp[idx]--;
            cur_time++;
            if(temp[idx] == 0) {
                ct[idx] = cur_time;
                count++;
            }
        } else cur_time++;
    }

    printf("\nP\tAT\tBT\tPri\tCT\tTAT\tWT\n");
    for(i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
        total_tat += tat[i];
        total_wt += wt[i];
        printf("P%d\t%d\t%d\t%d\t%d\t%d\t%d\n", i+1, at[i], bt[i], pri[i], ct[i], tat[i], wt[i]);
    }
    printf("\nAvg TAT: %.2f\nAvg WT: %.2f\n", total_tat/n, total_wt/n);
    return 0;
}
