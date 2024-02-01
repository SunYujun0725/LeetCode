/*
 * @Author: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @Date: 2024-02-01 14:07:23
 * @LastEditors: SunYujun0725 91317039+SunYujun0725@users.noreply.github.com
 * @LastEditTime: 2024-02-01 15:26:25
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

// insertNodeAtHead
void insertNodeAtHead(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
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

// mergeTwoLists
struct Node* mergeTwoLists(struct Node* list1, struct Node* list2) {
    struct Node* current1 = list1;
    struct Node* current2 = list2;
    struct Node* mergelist = NULL;
    while (current1 != NULL && current2 != NULL) {
        if (current1->data < current2->data) {
            insertNodeAtTail(&mergelist, current1->data);
            current1 = current1->next;
        } else if (current1->data == current2->data) {
            insertNodeAtTail(&mergelist, current1->data);
            insertNodeAtTail(&mergelist, current2->data);
            current1 = current1->next;
            current2 = current2->next;
        } else {
            insertNodeAtTail(&mergelist, current2->data);
            current2 = current2->next;
        }
    }
    if (current1 != NULL) {
        while (current1 != NULL) {
            insertNodeAtTail(&mergelist, current1->data);
            current1 = current1->next;
        }
    } else {
        while (current2 != NULL) {
            insertNodeAtTail(&mergelist, current2->data);
            current2 = current2->next;
        }
    }

    return mergelist;
}

int main() {
    //
    struct Node* head1 = NULL;

    // 插入一些数据到链表头
    insertNodeAtHead(&head1, 2);
    insertNodeAtHead(&head1, 1);

    // 插入一些数据到链表尾
    insertNodeAtTail(&head1, 4);
    insertNodeAtTail(&head1, 6);
    //
    struct Node* head2 = NULL;

    // 插入一些数据到链表头
    insertNodeAtHead(&head2, 3);
    insertNodeAtHead(&head2, 1);
    // 插入一些数据到链表尾
    insertNodeAtTail(&head2, 4);
    insertNodeAtTail(&head2, 5);
    insertNodeAtTail(&head2, 7);
    insertNodeAtTail(&head2, 8);
    struct Node* mergelist = mergeTwoLists(head1, head2);
    printList(head1);
    printList(head2);
    printList(mergelist);

    // deleteList(&head1);
    // deleteList(&head2);
    return 0;
}
