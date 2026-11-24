#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,n,fact=1,i;
    printf("Enter a positive integer: ");
    scanf("%d", &a);
    n=a;
    top:fact*=a;
    a--;
    if (a>0){ goto top;}
    printf("The factorial of %d is: %d .\n",n,fact);
    return 0;
}
