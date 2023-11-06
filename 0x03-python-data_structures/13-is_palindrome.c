#include "lists.h"

/**
 * pan - checks if a sin
 * @head: pointer to 
 * Return: 0 if it is not
 */
int pan(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (pan(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a s
 * @head: pointer t
 * Return: 0 if it is not a palind
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (pan(head, *head));
}
