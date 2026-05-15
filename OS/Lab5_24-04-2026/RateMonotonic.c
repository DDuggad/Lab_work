#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    float c[10], t[10], u = 0, b;

    printf("Enter number of tasks: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("Task %d (C and T): ", i + 1);
        scanf("%f %f", &c[i], &t[i]);
        u += (c[i] / t[i]);
    }

    b = n * (pow(2, 1.0 / n) - 1);
    printf("\nUtilization (U): %.2f", u);
    printf("\nRMS Bound: %.2f\n", b);

    if (u <= b) printf("Result: Tasks are Schedulable\n");
    else printf("Result: Tasks are NOT Schedulable\n");

    return 0;
}
/* Output:
Enter number of tasks: 3
Task 1 (C and T): 3 20
Task 2 (C and T): 2 5
Task 3 (C and T): 2 10

Utilization (U): 0.75
RMS Bound: 0.78
Result: Tasks are Schedulable
*/