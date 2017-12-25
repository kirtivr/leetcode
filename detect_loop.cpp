#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* next;
};

void push(struct Node** head_ref, int new_data) {
  struct Node* new_node =
    (struct Node*) malloc(sizeof(struct Node));

  new_node->data = new_data;
  new_node->next = (*head_ref);

  (*head_ref) = new_node;
}

int detectLoop(struct Node *list)
{
  struct Node * slow = list;
  struct Node * fast = list;

  while(slow && fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    if(slow == fast) {
      printf("Found loop");
      return 1;
    }
  }

  return 0;
}

int main() {
  struct Node* head = NULL;

  push(&head, 20);
  push(&head, 30);
  push(&head, 10);
  push(&head, 50);

  head->next->next->next = head;

  detectLoop(head);

  return 0;
}
