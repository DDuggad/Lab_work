#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, reverse=0;
    printf("Enter a integer: ");
    scanf("%d",&num);
    while (num!=0){
        int digit;
        digit=num%10;
        reverse=reverse*10+digit;
        num=num/10;
    }
    printf("The reversed number is: %d",reverse);
}
