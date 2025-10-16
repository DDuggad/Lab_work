#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len;
    printf("Enter a string: ");
    char s1[10];
    gets(s1);
    strrev(s1);
    printf("The reversed string is: %s", s1);
    return 0;

}
