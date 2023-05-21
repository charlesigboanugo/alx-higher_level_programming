#include "lists.h"
#include <stdlib.h>

/**
*
*/

int list_len(listint_t *ptr)
{
	int len;

	for (len = 0; ptr != NULL; ptr = ptr->next)
		len++;
	return len;
}

/**
*
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
	len = list_len(ptr);
	for (i = 0; i < len / 2; i++)
	{
		end = ptr;
		for (j = 1; j < len - 2 * (i); j++)
			end = end->next;
		if (ptr->n != end->n)
			return (0);
	}
	return (1);
}
