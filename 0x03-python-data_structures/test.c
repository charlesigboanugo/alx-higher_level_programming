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
	end = ptr;
	for (i = 0, j = 1; i < len / 2; j++, end = end->next)
	{
		if (j == len - 2 * (i))
		{
			if (ptr->n != end->n)
				return (0);
			ptr = ptr->next;
			end = ptr;
			i++;
			j = 1;
		}
	}
	return (1);
}
