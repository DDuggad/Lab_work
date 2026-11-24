#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,fact=1,i;
    printf("Enter a positive integer: ");
    scanf("%d", &a);
    for (i=1;i<=a;i++){
        fact=fact*i;
    }
    printf("The factorial of %d is: %d ",a,fact);
}
