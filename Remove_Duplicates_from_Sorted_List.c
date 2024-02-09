#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

// createNode
struct ListNode* createNode(int data) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->val = data;
    newNode->next = NULL;
    return newNode;
}

// insertNodeAtHead
void insertNodeAtHead(struct ListNode** head, int data) {
    struct ListNode* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}
 
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* cur;
    struct ListNode* prev;
    int cmp_num = -101;
    for (cur = head, prev = NULL; cur != NULL; prev = cur, cur = cur->next){
        if (cmp_num == cur->val){
            //delet
            prev->next = cur->next;
            free(cur);
            cur = prev;
        }
        else{
            cmp_num = cur->val;
        }
    }
    return head;
}
// printList
void printList(struct ListNode* head) {
    struct ListNode* current = head;
    while (current != NULL) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

int main() {
    //
    struct ListNode* head = NULL;
    // 插入一些数据到链表头
    insertNodeAtHead(&head, 3);
    insertNodeAtHead(&head, 3);
    insertNodeAtHead(&head, 2);
    insertNodeAtHead(&head, 1);
    insertNodeAtHead(&head, 1);

    head = deleteDuplicates(head);
    printList(head);
    
    return 0;
}
