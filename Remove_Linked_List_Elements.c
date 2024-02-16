/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-02-01 14:07:23
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-02-16 21:54:27
 * @FilePath: /vscode_cpp_for_Mac-master/a.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

// createNode
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// insertNodeAtTail
void insertNodeAtTail(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
        return;
    }

    struct Node* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;
}
// printList
void printList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }
    printf("\n");
}

// deleteList
void deleteList(struct Node** head) {
    struct Node* current = *head;
    struct Node* next;
    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    *head = NULL;
}
struct Node* removeElements(struct Node* head, int val) {
    struct Node* cur = head;
    struct Node* tmp = NULL;
    struct Node* prev = NULL;
    
    while(cur != NULL){
        if  (cur->data == val){
            if (prev == NULL){
                head = head->next;
                cur = head;
            }
            else{
                prev->next = cur->next;
                tmp = cur;
                cur = cur->next;
                free(tmp);
            }
        }
        else{
            prev = cur;
            cur = cur->next;
        }
    }
    
    printList(head);
    return head;
}
int main() {
    //
    struct Node* head1 = NULL;
    int val = 6;

    // 插入一些数据到链表尾
    insertNodeAtTail(&head1, 6);
    insertNodeAtTail(&head1, 2);
    insertNodeAtTail(&head1, 6);
    insertNodeAtTail(&head1, 3);
    insertNodeAtTail(&head1, 4);
    insertNodeAtTail(&head1, 5);
    insertNodeAtTail(&head1, 6);
    removeElements(head1, val);
    

    // deleteList(&head1);
    // deleteList(&head2);
    return 0;
}