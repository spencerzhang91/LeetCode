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
    list = createList(10);
    displayList(list);

    return 0;
}

struct ListNode *oddEvenList(struct ListNode *head)
{
    struct ListNode *Ohead, *Otracker = head;
    struct ListNode *Ehead, *Etracker = head->next;
    while (Otracker || Etracker)
    {
        Otracker->next = Etracker->next;
        Otracker = (Otracker->next)? Otracker->next: Otracker;
        Etracker->next = (Etracker->next)? Otracker->next: NULL;
        Etracker = Etracker->next;
    }
    Otracker->next = Ehead;
    return head;
}

void displayList(struct ListNode *head)
{
    while (head)
    {
        printf("%d ", head->val);
        head = head->next;
    }
}

struct ListNode *createList(int node_num)
{
    /* This function creates linked list with given nodes and acsending val */
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