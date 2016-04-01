// 328 Odd Even Linked List

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

int main(void)
{
    /* --- */
}

struct ListNode* oddEvenList(struct ListNode* head)
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
    /* --- */
}