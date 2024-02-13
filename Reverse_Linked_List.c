/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-02-01 19:48:33
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-02-13 21:51:53
 * @FilePath: /vscode_cpp_for_Mac-master/Reverse_Linked_List.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode* next;
};

// createNode
struct ListNode* createNode(int data) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}
// insertNodeAtHead
void insertNodeAtHead(struct ListNode** head, int data) {
    struct ListNode* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// insertNodeAtTail
void insertNodeAtTail(struct ListNode** head, int data) {
    struct ListNode* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }

    struct ListNode* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
}
// printList
void printList(struct ListNode* head) {
    struct ListNode* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* current = head;
    struct ListNode* Reverse = NULL;
    while(current != NULL){
        insertNodeAtHead(&Reverse, current->data);
        current = current->next;
    }
    return Reverse;
}


int main() {
    //
    struct ListNode* head1 = NULL;
    struct ListNode* ans = NULL;
    // 插入一些数据到链表尾
    insertNodeAtTail(&head1, 1);
    insertNodeAtTail(&head1, 2);
    insertNodeAtTail(&head1, 3);
    insertNodeAtTail(&head1, 4);
    insertNodeAtTail(&head1, 5);
    reverseList(head1);

    //printList(ans);
    return 0;
}
