#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void add(struct Node** head, int val) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = val; n->next = NULL;
    if (!*head) { *head = n; return; }
    struct Node* t = *head;
    while (t->next) t = t->next;
    t->next = n;
}

void show(struct Node* t) {
    while (t) { printf("%d ", t->data); t = t->next; }
    printf("\n");
}

void sort(struct Node* head) {
    for (struct Node* i = head; i; i = i->next)
        for (struct Node* j = i->next; j; j = j->next)
            if (i->data > j->data) {
                int tmp = i->data; i->data = j->data; j->data = tmp;
            }
}

void reverse(struct Node** head) {
    struct Node *p = NULL, *c = *head, *n;
    while (c) { n = c->next; c->next = p; p = c; c = n; }
    *head = p;
}

int main() {
    struct Node *l1 = NULL, *l2 = NULL;
    add(&l1, 30); add(&l1, 10); add(&l1, 20);
    add(&l2, 50); add(&l2, 40);

    printf("L1: "); show(l1);
    sort(l1); printf("Sorted: "); show(l1);
    reverse(&l1); printf("Reversed: "); show(l1);

    struct Node* t = l1;
    while (t->next) t = t->next;
    t->next = l2;
    printf("Concatenated: "); show(l1);
    return 0;
}