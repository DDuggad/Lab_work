#include <stdio.h>
#include <stdlib.h>

int main()
{
    struct student{
        char usn[11];
        char name[15];
        int marks;
    };
    struct student s1;

    printf("Enter USN, Name & Marks: ");
    scanf("%s%s%d", s1.usn , s1.name,&s1.marks);
    printf("The entered USN: %s \nName: %s\nMarks: %d ",s1.usn, s1.name,s1.marks);
    return 0;
}
int add (a,b){
return a+b;
}
