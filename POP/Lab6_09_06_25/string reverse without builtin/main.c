#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len;
    int i=0,j=0;
    printf("Enter a string: ");
    char a[10],b[10];
    gets(a);
    while(a[i]!='\0'){i++;}i--;
    for(j=0;j<=i;j++){
        b[j]=a[i-j];
    }
    b[j+1]='\0';
    printf("The reversed string is: %s", b);
    return 0;

}
