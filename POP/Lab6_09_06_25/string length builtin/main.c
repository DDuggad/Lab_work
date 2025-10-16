#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len;
    printf("Enter a string: ");
    char s1[10];
    gets(s1);
    len=strlen(s1);
    printf("The length of %s is : %d.",s1,len);
    return 0;

}
