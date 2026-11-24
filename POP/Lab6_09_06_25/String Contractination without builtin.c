#include <stdio.h>
#include <stdlib.h>

int main()
{
    char a[20], b[10];
    int i=0,j=0;
    printf("Enter string 1: ");
    gets(a);
    printf("Enter string 2: ");
    gets(b);
    while(a[i]!='\0'){i++;}
    while(b[j]!='\0'){
        a[i]=b[j];
        j++;
        i++;
    }
    a[i]='\0';
    printf("The new string is: %s",a);
    return 0;

}
