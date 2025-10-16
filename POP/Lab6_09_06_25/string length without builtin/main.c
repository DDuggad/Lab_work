#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len=0;
    printf("Enter a string: ");
    char s2[10];
    gets(s2);
    while (s2[len]!='\0'){len++;}
    printf("The length of %s is : %d.",s2,len);
    return 0;

}

struct stud{
    int rno;
    char name[10];
    char chourse[10];
    };

