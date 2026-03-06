#include <stdio.h>
#include<stdlib.h>
int main(){
    int n,i,time=0;
    int at[10],bt[10],ct[10],tat[10],wt[10];
    float avg_wt=0,avg_tat=0;
    printf("Enter no of process: ");
    scanf("%d",&n);
    printf("Enter Arrival Time of each process in sequence: ");
    for (i=0;i<n;i++){
        scanf("%d",&at[i]);
    }
    printf("Enter Burst Time of each process in sequence: ");
    for (i=0;i<n;i++){
        scanf("%d",&bt[i]);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[i] > at[j]) {
                int temp = at[i]; at[i] = at[j]; at[j] = temp;
                temp = bt[i]; bt[i] = bt[j]; bt[j] = temp;
            }
        }
    }
    printf("\nProcess\tAT\tBT\tCT\tTAT\tWT");
    for (i=0;i<n;i++){
        if (time<at[i]){time=at[i];}
        ct[i]=time+bt[i];
        tat[i]=ct[i]-at[i];
        wt[i]=tat[i]-bt[i];
        time+=bt[i];
        avg_wt+=wt[i];avg_tat+=tat[i];
        printf("\nP%d\t%d\t%d\t%d\t%d\t%d",i+1,at[i],bt[i],ct[i],tat[i],wt[i]);
        
    }
    avg_wt/=n;avg_tat/=n;
    printf("\nAvg Waiting Time: %.2f\nAvg Turn Around Time: %.2f",avg_wt,avg_tat);
}
