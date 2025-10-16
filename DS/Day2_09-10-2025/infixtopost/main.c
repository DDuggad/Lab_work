#include <stdio.h>
#include <stdlib.h>
int top1=-1, top2=-1, top3=-1 ;
char stack1[25], stack2[25], stack3[25];
void push (char a, int c){
    if (c==1){top1+=1; stack1[top1]=a;}
    else if (c==2){top2+=1; stack2[top2]=a;}
}
char pop (){return stack2[top2--];}
int main(){
    printf("Enter infix expression (length less than 20): ");
    gets(stack3);
    top3=0;
    for (top3=0;stack3[top3]!='\0';top3++){
        char a = stack3[top3];
        if ((a >= 'a' && a <= 'z') || (a >= 'A' && a <= 'Z') || (a >= '0' && a <= '9')){
            push(a,1);
        }
        else if (a=='('){push(a,2);}
        else if (a==')'){
            while (stack2[top2]!='('){
                char b = pop();
                push(b,1);
            }
            pop();
        }
        else if (a=='*' || a == '/'){
            if (top2 > -1 && (stack2[top2]=='*' || stack2[top2] == '/')){
                char b = pop();
                push(b,1);
            }
            push(a,2);
        }
        else if (a=='+' || a=='-'){
            while (top2 > -1 &&(stack2[top2]=='*' || stack2[top2]=='/' || stack2[top2]=='+' || stack2[top2]=='-')){
                char b = pop();
                push (b,1);
            }
            push(a,2);
        }
    }
    while (top2 > -1) {
        char b = pop();
        push(b, 1);
    }
    push('\0',1);
    printf("The postfix equation is: %s ",stack1);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
int top1=-1, top2=-1, top3=-1 ;
char stack1[25], stack2[25], stack3[25];
void push (char a, int c){
    if (c==1){top1+=1; stack1[top1]=a;}
    else if (c==2){top2+=1; stack2[top2]=a;}
}
char pop (){return stack2[top2--];}
int main(){
    printf("Enter infix expression (length less than 20): ");
    gets(stack3);
    top3=0;
    for (top3=0;stack3[top3]!='\0';top3++){
        char a = stack3[top3];
        if ((a >= 'a' && a <= 'z') || (a >= 'A' && a <= 'Z') || (a >= '0' && a <= '9')){
            push(a,1);
        }
        else if (a=='('){push(a,2);}
        else if (a==')'){
            while (stack2[top2]!='('){
                char b = pop();
                push(b,1);
            }
            pop();
        }
        else if (a=='*' || a == '/'){
            if (top2 > -1 && (stack2[top2]=='*' || stack2[top2] == '/')){
                char b = pop();
                push(b,1);
            }
            push(a,2);
        }
        else if (a=='+' || a=='-'){
            while (top2 > -1 &&(stack2[top2]=='*' || stack2[top2]=='/' || stack2[top2]=='+' || stack2[top2]=='-')){
                char b = pop();
                push (b,1);
            }
            push(a,2);
        }
    }
    while (top2 > -1) {
        char b = pop();
        push(b, 1);
    }
    push('\0',1);
    printf("The postfix equation is: %s ",stack1);

    return 0;
}
