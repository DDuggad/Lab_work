#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a=0,b=1,c,d=0,e;
    printf("Enter the range: ");
    scanf("%d",&c);
    while (c!=d){
        printf("%d ",a);
        d++;
        e=b+a;
        a=b;
        b=e;
    }
}
