#include <stdio.h>
#include <stdlib.h>

struct Listnode {
    int val;
    struct Listnode* next;
};

// createNode
struct Listnode* createNode(int val) {
    struct Listnode* newNode = (struct Listnode*)malloc(sizeof(struct Listnode));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

// insertNodeAtTail
void insertNodeAtTail(struct Listnode** head, int val) {
    struct Listnode* newNode = createNode(val);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    struct Listnode* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

struct Listnode* addTwoNumbers(struct Listnode* l1, struct Listnode* l2) {
    struct Listnode* current1 = l1;
    struct Listnode* current2 = l2;
    struct Listnode* new_head = NULL;
    int carry_in = 0;
    while (current1 != NULL && current2 != NULL) {
        if (current1->val + current2->val + carry_in < 10) {
            insertNodeAtTail(&new_head, current1->val + current2->val + carry_in);
            carry_in = 0;
        } else {
            insertNodeAtTail(&new_head, current1->val + current2->val + carry_in - 10);
            carry_in = 1;
        }
        current1 = current1->next;
        current2 = current2->next;
    }
    if (current1 != NULL) {
        while (current1 != NULL) {
            if (current1->val + carry_in < 10) {
                insertNodeAtTail(&new_head, current1->val + carry_in);
                carry_in = 0;
            } else {
                insertNodeAtTail(&new_head, current1->val + carry_in - 10);
                carry_in = 1;
            }
            current1 = current1->next;
        }
    } else {
        while (current2 != NULL) {
            if (current2->val + carry_in < 10) {
                insertNodeAtTail(&new_head, current2->val + carry_in);
                carry_in = 0;
            } else {
                insertNodeAtTail(&new_head, current2->val + carry_in - 10);
                carry_in = 1;
            }
            current2 = current2->next;
        }
    }
    if (carry_in == 1) {
        insertNodeAtTail(&new_head, 1);
    }

    return new_head;
}

// printList
void printList(struct Listnode* head) {
    struct Listnode* current = head;
    while (current != NULL) {
        printf("%d ", current->val);
        current = current->next;
    }
    printf("\n");
}

int main() {
    struct Listnode* head1 = NULL;
    // 插入一些数据到链表尾
    insertNodeAtTail(&head1, 2);
    insertNodeAtTail(&head1, 4);
    insertNodeAtTail(&head1, 9);

    struct Listnode* head2 = NULL;
    // 插入一些数据到链表尾
    insertNodeAtTail(&head2, 5);
    insertNodeAtTail(&head2, 6);
    insertNodeAtTail(&head2, 4);
    insertNodeAtTail(&head2, 9);
    struct Listnode* new_head = addTwoNumbers(head1, head2);
    printList(new_head);

    return 0;
}
