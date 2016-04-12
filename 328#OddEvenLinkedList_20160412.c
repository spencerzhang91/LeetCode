// 328 Odd Even Linked List
// Definition for singly-linked list.
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *oddEvenList(struct ListNode *head);
void displayList(struct ListNode *head);
struct ListNode *createList(int node_num);

int main(void)
{
    /* This main function is for testing. */
    struct ListNode *list;
    list = createList(0);
    displayList(list);
    struct ListNode *altered;
    altered = oddEvenList(list);
    displayList(altered);

    return 0;
}

struct ListNode *oddEvenList(struct ListNode *head)
{
    struct ListNode *oddPtr = head;
    struct ListNode *eveHead, *evePtr, *curr;
    eveHead = evePtr = curr = (head)? head->next: NULL;
    int counter = 2; // curr starts as an even node (second node if any)
    while (curr)
    {
        counter++;
        if (counter % 2 != 0)
        {
            oddPtr->next = curr->next;
            oddPtr = (oddPtr->next)? oddPtr->next: oddPtr;
        }
        else
        {
            evePtr->next = curr->next;
            evePtr = evePtr->next;
        }
        curr = curr->next;
    }
    if (oddPtr)
        oddPtr->next = eveHead;
    return head;
}

void displayList(struct ListNode *head)
{
    if (!head)
    	printf("Empty list.");
    while (head)
    {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

struct ListNode *createList(int node_num)
{
    /* This function creates linked list with given nodes and acsending val */
    if (!node_num) return NULL;
    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->val = 1; head->next = NULL;
    struct ListNode *curr = head;
    for (int i = 1; i < node_num; i++)
    {
        struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
        temp->val = 1 + i; temp->next = NULL;
        curr->next = temp;
        curr = curr->next;
    }
    return head;
}