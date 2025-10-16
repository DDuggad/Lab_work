#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s1[20], s2[10];
    printf("Enter string 1: ");
    gets(s1);
    printf("Enter string 2: ");
    gets(s2);
    strcat(s1,s2);
    printf("The new string is: %s",s1);
    return 0;

}
