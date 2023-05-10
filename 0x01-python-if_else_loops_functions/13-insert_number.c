#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: Number to be inserted.
 *
 * Return: Address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;
	/*check if the head pointer is NULL*/
	if (head == NULL)
		return (NULL);
	/*allocate memory for the new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	/* assign the number to the new node*/
	new_node->n = number;
	new_node->next = NULL;

	/*if the list is empty or num is smaller thatn current head value*/
	if (*head == NULL || number < (*head)->n)
	{
		/* insert the new node at the beginning of the list*/
		new_node->next = *head;
		*head = new_node;
	return (new_node);
	}
	/*find the appropriate position to the insert the new node*/
	current = *head;
	while (current->next != NULL && number > current->next->n)
		current = current->next;
	/*insert the new node into the list*/
	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
