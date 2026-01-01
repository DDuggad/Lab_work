#include <stdio.h>
#include <stdlib.h>
struct Node{
    struct Node* prev;
    int data;
    struct Node* next;
};
struct Node* head=NULL;
void insert (int value){
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    newNode->data=value;
    newNode->prev=NULL;
    newNode->next=head;
    if(head!=NULL){
        head->prev=newNode;
    }
    head=newNode;
    return;
}
void del(int value) {
    struct Node* temp = head;
    while (temp != NULL && temp->data != value) {temp = temp->next;}
    if (temp == NULL){printf("Data not found!\n");return;}
    if (temp == head){head = temp->next;}
    else{temp->prev->next=temp->next;}

    if (temp->next != NULL){temp->next->prev = temp->prev;}
    free(temp);
}
void display(){
    struct Node* temp=head;
    printf("NULL <- ");
    while(temp!=NULL){
        printf("%d -> ",temp->data);
        temp=temp->next;
    }
    printf("NULL\n");
}
int main(){
    int choice=0;int temp1;
    printf("Enter 1 to enter\n2 to delete a value\n3 to Display\n4 to exit: ");
    scanf("%d",&choice);
    while(choice!=4){
        if (choice==1){
            printf("Enter a value: ");
            scanf("%d",&temp1);
            insert(temp1);
        }
        else if(choice==2){
            printf("Enter a value: ");
            scanf("%d",&temp1);
            del(temp1);
        }
        else if(choice==3){display();}
        else {printf("Enter a valid choice.");}
        printf("Enter a new choice: ");
        scanf("%d",&choice);
    }
    return 0;
}
