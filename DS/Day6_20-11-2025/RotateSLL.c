struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (head==NULL || head->next==NULL) return head;
    if (k<=0) return head;
    struct ListNode* temp = head; int t=1;
    while(temp->next!=NULL){temp=temp->next;t++;}
    k=k%t;
    for (int i=0;i<k;i++){
        struct ListNode* temp = head;
        while(temp->next->next!=NULL){temp=temp->next;}
        temp->next->next=head;
        head=temp->next;
        temp->next=NULL;
    }
    return head;
    
}
