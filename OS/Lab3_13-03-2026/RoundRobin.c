#include <stdio.h>

int main() {
    int n, i, qt, count = 0, temp[10], cur_time = 0;
    int at[10], bt[10], ct[10], tat[10], wt[10];
    float total_wt = 0, total_tat = 0;

    printf("Enter number of processes & Time Quantum: ");
    scanf("%d %d", &n, &qt);

    for(i = 0; i < n; i++) {
        printf("P%d AT & BT: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        temp[i] = bt[i]; // Store original BT in temp
    }

    while(count < n) {
        int flag = 0;
        for(i = 0; i < n; i++) {
            if(temp[i] > 0 && at[i] <= cur_time) {
                flag = 1;
                if(temp[i] > qt) {
                    cur_time += qt;
                    temp[i] -= qt;
                } else {
                    cur_time += temp[i];
                    ct[i] = cur_time;
                    temp[i] = 0;
                    count++;
                }
            }
        }
        if(!flag) cur_time++; // If no process arrived, increment time
    }

    printf("\nP\tAT\tBT\tCT\tTAT\tWT\n");
    for(i = 0; i < n; i++) {
        tat[i] = ct[i] - at[i];
        wt[i] = tat[i] - bt[i];
        total_tat += tat[i];
        total_wt += wt[i];
        printf("P%d\t%d\t%d\t%d\t%d\t%d\n", i+1, at[i], bt[i], ct[i], tat[i], wt[i]);
    }
    printf("\nAvg TAT: %.2f\nAvg WT: %.2f\n", total_tat/n, total_wt/n);
    return 0;
}
