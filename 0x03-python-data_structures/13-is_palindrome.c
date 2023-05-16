#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL;
	listint_t *curr = slow->next;

	while (curr != NULL)
	{
		listint_t *next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	while (slow != NULL && prev != NULL)
	{
		if (slow->data != prev->data)
		{
			return(0);
		}
		slow = slow->next;
		prev = prev->next;
	}
	return(1);
}
