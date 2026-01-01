struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode flist;
    flist.val=0;
    flist.next=NULL;
    struct ListNode* current = &flist;
    if (list1==NULL) return list2;
    if (list2==NULL) return list1;
    while (list1 !=NULL && list2!=NULL ){
        if (list1->val <= list2->val){
            current->next=list1;
            list1=list1->next;
        }
        else if (list2->val < list1->val){
            current->next=list2;
            list2=list2->next;
        }
        current=current->next;

    }
    while (list1 !=NULL || list2!=NULL ){
        if (list1!=NULL){
            current->next=list1;
            list1=list1->next;
        }
        else if (list2!=NULL){
            current->next=list2;
            list2=list2->next;
        }
        current=current->next;
    }

    return flist.next;
}
