#include <stdio.h>

int main() {
    int sn, un, i, sbt[10], ubt[10], swt[10], uwt[10], stat[10], utat[10];

    printf("Enter no. of System and User processes: ");
    scanf("%d %d", &sn, &un);

    for (i = 0; i < sn; i++) {
        printf("System P%d BT: ", i + 1);
        scanf("%d", &sbt[i]);
    }
    for (i = 0; i < un; i++) {
        printf("User P%d BT: ", i + 1);
        scanf("%d", &ubt[i]);
    }

    swt[0] = 0;
    for (i = 1; i < sn; i++) swt[i] = swt[i - 1] + sbt[i - 1];
    for (i = 0; i < sn; i++) stat[i] = swt[i] + sbt[i];

    uwt[0] = (sn > 0) ? stat[sn - 1] : 0;
    for (i = 1; i < un; i++) uwt[i] = uwt[i - 1] + ubt[i - 1];
    for (i = 0; i < un; i++) utat[i] = uwt[i] + ubt[i];

    printf("\nType\tP\tBT\tWT\tTAT\n");
    for (i = 0; i < sn; i++)
        printf("Sys\tS%d\t%d\t%d\t%d\n", i + 1, sbt[i], swt[i], stat[i]);
    for (i = 0; i < un; i++)
        printf("User\tU%d\t%d\t%d\t%d\n", i + 1, ubt[i], uwt[i], utat[i]);

    return 0;
}