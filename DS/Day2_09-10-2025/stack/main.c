#include <stdio.h>
#include <stdlib.h>

int main()
{
    int stack[10];
    int top=-1;
    printf("The empty stack is created.");
    int user_choice=0;
    while(user_choice!=-1){
        printf("Enter 1 to push, 2 to pop, 3 to display & -1 to end the program: ");
        scanf("%d",&user_choice);
        if (user_choice==1 && top ==5){printf("Stack Overflow.\n");}
        else if (user_choice==2 && top ==-1){printf("Stack Underflow.\n");}
        else if (user_choice==1){
            printf("Enter a element: ");
            top+=1;
            scanf("%d",&stack[top]);
        }
        else if (user_choice==2){top-=1;}
        else if (user_choice==3){
            for (int i=top;i>=0;i--){
                printf("%d\n",stack[i]);
            }
        }
        else if (user_choice==-1){break;}
    }
    printf("Thank You");

    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int stack[10];
    int top=-1;
    printf("The empty stack is created.");
    int user_choice=0;
    while(user_choice!=-1){
        printf("Enter 1 to push, 2 to pop, 3 to display & -1 to end the program: ");
        scanf("%d",&user_choice);
        if (user_choice==1 && top ==5){printf("Stack Overflow.\n");}
        else if (user_choice==2 && top ==-1){printf("Stack Underflow.\n");}
        else if (user_choice==1){
            printf("Enter a element: ");
            top+=1;
            scanf("%d",&stack[top]);
        }
        else if (user_choice==2){top-=1;}
        else if (user_choice==3){
            for (int i=top;i>=0;i--){
                printf("%d\n",stack[i]);
            }
        }
        else if (user_choice==-1){break;}
    }
    printf("Thank You");

    return 0;
}
