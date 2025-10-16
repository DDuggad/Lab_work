#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    float sum=0,i;

    printf("Enter value of n: ");
    scanf("%d",&n);
    for (i=1.0;i<=n;i++){
        sum = sum + (1/i);
    }
    printf("The sum of the series upto 1/n is : %.2f ",sum);
    return 0;
}
