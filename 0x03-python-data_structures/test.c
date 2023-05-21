#include "lists.h"
#include <stdlib.h>

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: stores the pointer to the list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *ptr, *end;
	int i, j, len;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ptr = *head;
	for (len = 0; ptr != NULL; ptr = ptr->next)
		len++;
	ptr = *head;
	for (i = 0; i < len / 2; i++, ptr = ptr->next)
	{
		end = ptr;
		for (j = 1; j < len - 2 * (i); j++)
			end = end->next;
		if (ptr->n != end->n)
			return (0);
	}
	return (1);
}
