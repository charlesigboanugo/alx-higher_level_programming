#include "lists.h"
#include <stdlib.h>

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to a linked list
* @number: value to insert
*
* Return: the address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *prev = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(*new))
	if (new == NULL)
		return (NULL);
	new->n = number;
	for (; *head != NULL; head = head->next)
	{
		if ((*head)->n > number)
			break;
		prev = *head;
	}
	if (prev != NULL)
	{
		prev->next = new;
	}
	else



}
