#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int bin,dec,i=0;
    printf("Enter a number in binary unsigned: ");
    scanf("%d",&bin);
    while(bin!=0){
        int num=0;
        num=bin%10;
        bin=bin/10;
        dec=dec+(num*pow(2,i));
        i++;

    }
    printf("The decimal number is: %d ",dec);
}
