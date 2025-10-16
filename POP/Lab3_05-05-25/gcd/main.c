#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,b,rem;
    printf("Enter two number: ");
    scanf("%d %d",&a,&b);
    while (b!=0){
        rem=a%b;
        a=b;
        b=rem;
    }
    printf("The gcd of given number is : %d ",a);
}
