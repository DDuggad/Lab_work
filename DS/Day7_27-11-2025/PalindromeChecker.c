/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    struct ListNode* temp = head;
    int arr[100000]; 
    int size = 0;
    while (temp != NULL) {
        arr[size++] = temp->val;
        temp = temp->next;
    }
    int left=0;int right=size-1;
    while(left<=right){
        if (arr[left]!=arr[right]) return false;
        left++;right--;
    }
    return true;
}
