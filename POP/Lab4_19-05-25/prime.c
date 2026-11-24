#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a,i,p=0;
    printf("Enter a number: ");
    scanf("%d",&a);
    for (i=2;i<a;i++){
        if (a%i==0){p+=1;}

    }
    if (p==0){printf("Prime Number. \n");}
    else {printf("Not a Prime Number. \n");}
}
