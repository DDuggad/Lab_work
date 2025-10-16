#include <stdio.h>
#include <stdlib.h>

int main()
{
    int ran,ex,i=0;
    printf("Enter a range: ");
    scanf("%d",&ran);
    printf("Enter number to be excluded (less than range) : ");
    scanf("%d",&ex);
    while (0==0) {
        i++;
        if (i==ex){continue;}
        if (i==ran){break;}
        printf("%d ",i);
    }
    return 0;
}
