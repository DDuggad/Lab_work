#include <stdio.h>
#include <stdlib.h>

int main()
{
    char s1[20], s2[10];
    int res;
    printf("Enter string 1: ");
    gets(s1);
    printf("Enter string 2: ");
    gets(s2);
    res=strcmp(s1,s2);
    if (res==0){printf("Both are equal.");}
    else if (res<0){printf("First String is greater. ");}
    else {printf("Second String is greater.");}
    return 0;

}
