#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* head = NULL;

void in_b(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}

void in_e(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;

    if (head == NULL) {head = newNode;return;}

    struct Node* ptr = head;
    while (ptr->next != NULL) {ptr = ptr->next;}
    ptr->next = newNode;
}

void in_p(int data, int pos) {
    if (pos == 1) {
        in_b(data);
        return;
    }

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;

    struct Node* temp = head;
    for (int i = 1; i < pos - 1 && temp != NULL; i++) {
        temp = temp->next;
    }

    if (temp == NULL) {
        printf("Invalid position. Appending to end.\n");
        in_e(data);
    } else {
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void display() {
    struct Node* ptr = head;
    if (ptr == NULL) {
        printf("List is empty.\n");
        return;
    }
    while (ptr != NULL) {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}

void swap(int pos1, int pos2) {
    if (pos1 == pos2) return;

    struct Node *arr1 = head;
    for (int i = 1; arr1 != NULL && i < pos1; i++) {
        arr1 = arr1->next;
    }

    struct Node *arr2 = head;
    for (int i = 1; arr2 != NULL && i < pos2; i++) {
        arr2 = arr2->next;
    }

    if (arr1 == NULL || arr2 == NULL) {
        printf("Any of the position is invalid.\n");
        return;
    }
    int a = arr1->data, b = arr2->data;
    arr1->data = b;
    arr2->data = a;
    printf("Swapped nodes at positions %d and %d.\n", pos1, pos2);
    return;
}

int main() {
    printf("List: ");
    display();

    printf("\nInserting 10 at beginning.\n30 at end.\n5 at beginning.\n20 at position 3.\n40 at invalid position 99.\n");
    in_b(10);
    in_e(30);
    in_b(5);
    in_p(20,3);
    in_p(40,99);
    printf("\nList: \n");
    display();
    printf("\n\n");
    swap(2,4);
    printf("List after swapping: \n");
    display();

    return 0;
}
